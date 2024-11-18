#!/usr/bin/env python3

# Tobias Senti <git@tsenti.li>

from pyverilog.vparser.parser import parse
import os
import subprocess

def clean_name(name):
    return name.replace('[', '_').replace(']', '_').replace('\\', '').replace('.', '_')

def part_design(filename, out_filename, partitions):
    ast, directives = parse(open(filename, 'r'))

    desc = ast.description
    defs = desc.definitions

    top_module = None
    for child in defs:
        if type(child).__name__ == 'ModuleDef':
            top_module = child
            break
    
    inputs = []
    outputs = []
    wires = []
    instances = []
    for item in top_module.items:
        if type(item).__name__ == 'Decl':
            for decl in item.list:
                if type(decl).__name__ == 'Input':
                    inputs.append(clean_name(decl.name))
                elif type(decl).__name__ == 'Output':
                    outputs.append(clean_name(decl.name))
                elif type(decl).__name__ == 'Wire':
                    wires.append(clean_name(decl.name))
        if type(item).__name__ == 'InstanceList':
            for instance in item.instances:
                ports = []
                for port in instance.portlist:
                    argname = port.argname
                    if type(argname).__name__ != 'Identifier':
                        continue
                    ports.append((port.portname, clean_name(port.argname.name)))
                params = {}
                for param in instance.parameterlist:
                    name = param.paramname
                    if len(param.children()) == 1:
                        value = param.children()[0].value.split("'")[1]
                        if value.startswith('d') or value.startswith('sd'):
                            value = int(value.split('d')[1], 10)
                        elif value.startswith('h'):
                            value = int(value.split('h')[1], 16)
                        elif value.startswith('b'):
                            value = int(value.split('b')[1], 2)
                        else:
                            continue
                        params[name] = value
                instances.append({
                    'name': clean_name(instance.name),
                    'module': clean_name(instance.module),
                    'ports': ports,
                    'params': params
                })
    
    instance_to_vertex_mapping = {}
    edges = {}
    for i, wire in enumerate(wires):
        # Find all instances that have this wire as an input/output
        vertices = []
        new_instance_to_vertex_mapping = instance_to_vertex_mapping.copy()
        for instance in instances:
            for port in instance['ports']:
                if port[1] == wire:
                    instance_name = instance['name']
                    if instance_name not in new_instance_to_vertex_mapping:
                        new_instance_to_vertex_mapping[instance_name] = 1 + len(new_instance_to_vertex_mapping)
                    vertices.append(instance_name)

        instance_to_vertex_mapping = new_instance_to_vertex_mapping

        edges[wire] = {
            'idx': i,
            'vertices': vertices
        }

    vertex_to_instance_mapping = {v: k for k, v in instance_to_vertex_mapping.items()}

    for edge in edges:
        print(edge, edges[edge])

    # Generate hypergraph file
    with open(out_filename, 'w') as f:
        f.write(f'{len(edges)} {len(instance_to_vertex_mapping)}\n')
        for edge in edges:
            for idx, vertex in enumerate(edges[edge]['vertices']):
                if idx > 0:
                    f.write(' ')
                f.write(f'{instance_to_vertex_mapping[vertex]}')
            f.write('\n')

    # Run tritonpart
    print('Running tritonpart')
    tcl_filename = out_filename + '.tcl'
    try:
        open(tcl_filename, 'w').write(f'''triton_part_hypergraph -hypergraph_file {out_filename} -num_parts {partitions}; exit;''')
        #result = subprocess.check_output(['openroad', tcl_filename, '-threads', 'max'], text=True)
        #print(result)
    finally:
        print('Done')
        #if os.path.exists(tcl_filename):
            #os.unlink(tcl_filename)
    
    # Read partitioning
    part_filename = out_filename + '.part.' + str(partitions)
    partitioning = []
    with open(part_filename, 'r') as f:
        for line in f:
            partitioning.append(int(line.strip()))

    partition_members = {}
    instance_name_to_partition = {}
    for idx in range(0, len(partitioning)):
        print(f'Instance {vertex_to_instance_mapping[idx + 1]} is in partition {partitioning[idx]}')
        instance_name = vertex_to_instance_mapping[idx + 1]
        partition_members[partitioning[idx]] = partition_members.get(partitioning[idx], []) + [instance_name]
        instance_name_to_partition[instance_name] = partitioning[idx]

    for partition in partition_members:
        print(f'Partition {partition} has members {len(partition_members[partition])} {partition_members[partition]}')

    wire_to_partition = {}
    for wire in wires:
        for instance in instances:
            for port in instance['ports']:
                if port[1] == wire:
                    instance_partition = instance_name_to_partition[instance['name']]
                    if wire not in wire_to_partition:
                        wire_to_partition[wire] = [instance_partition]
                    elif instance_partition not in wire_to_partition[wire]:
                        wire_to_partition[wire].append(instance_partition)
    
    for wire in wire_to_partition:
        wire_to_partition[wire].sort()
        print(f'Wire {wire} is in partitions {wire_to_partition[wire]}')

    partiton_count = [0] * int(partitions)
    crossing_wires = []
    for wire in wire_to_partition:
        partiton_count[len(wire_to_partition[wire])-1] += 1
        if len(wire_to_partition[wire]) > 1:
            crossing_wires.append(wire)
            print(f'Wire {wire} is crossing partitions {wire_to_partition[wire]}')

    print(f'Partition count: {partiton_count}')

    print(f'Found {len(crossing_wires)} crossing wires')

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Convert verilog to ABEL'
    )

    parser.add_argument('fin', help='Input file')
    parser.add_argument('fout', help='Output file')
    parser.add_argument('--partitions', help='Number of partitions', default=2)
    args = parser.parse_args()

    part_design(args.fin, args.fout, args.partitions)

if __name__ == '__main__':
    main()
