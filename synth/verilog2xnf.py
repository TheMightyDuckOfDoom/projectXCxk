#!/usr/bin/env python3

# Tobias Senti <git@tsenti.li>

from pyverilog.vparser.parser import parse

def clean_name(name):
    return name.replace('[', '_').replace(']', '_').replace('\\', '').replace('.', '_')

def run(filename, out_filename, device, package):
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

    pin_direction = {
        'IBUF': {
            'I': 'I',
            'O': 'O'
        },
        'OBUF': {
            'I': 'I',
            'O': 'O'
        },
        'DFF': {
            'C': 'I',
            'D': 'I',
            'CE': 'I',
            'RD': 'I',
            'Q': 'O'
        },
        'LUT': {
            'I0': 'I',
            'I1': 'I',
            'I2': 'I',
            'I3': 'I',
            'I4': 'I',
            'O': 'O'
        }
    }

    with open(out_filename, 'w') as f:
        f.write('LCANET, 5\n')
        f.write(f'PROG, VERILOG2XNF, 0.1, "Created from {filename}"\n')
        f.write(f'PART, {device}{package}\n\n')

        for input in inputs:
            f.write(f'EXT, {input}, I\n')
        f.write('\n')
        for output in outputs:
            f.write(f'EXT, {output}, O\n')
        f.write('\n')
        for wire in wires:
            if wire in inputs or wire in outputs:
                continue
            f.write(f'SIG, {wire}, X\n')

        f.write('\n')
        for instance in instances:
            if instance['module'] in ['IBUF', 'DFF', 'OBUF']:
                f.write(f'SYM, {instance["name"]}, {instance["module"]}\n')
                for port in instance['ports']:
                    f.write(f'PIN, {port[0]}, {pin_direction[instance["module"]][port[0]]}, {port[1]}\n')
                f.write('END\n')
            elif instance['module'] == 'LUT':
                lut_table = instance["params"]["INIT"]
                eqn = ''
                lut_k = instance["params"]["K"]
                max_val = 2**lut_k
                for i in range(0, max_val):
                    if (lut_table & (1 << i)) == 0:
                        continue
                    if len(eqn) > 0:
                        eqn += '+'
                    eqn += f'('
                    for k in range(0, lut_k):
                        if k > 0:
                            eqn += '*'
                        if i & (1 << k):
                            eqn += f'I{k}'
                        else:
                            eqn += f'(~I{k})'
                    eqn += ')'

                line = f'SYM, {instance["name"]}, EQN, EQN={eqn}\n'
                if len(line) >= 1024:
                    print(f'Warning: EQN too long for {instance["name"]}')
                    print(f'EQN={eqn}')
                    print(f'Length={len(line)}')
                    exit(1)
                f.write(line)
                for port in instance['ports']:
                    f.write(f'PIN, {port[0]}, {pin_direction[instance["module"]][port[0]]}, {port[1]}\n')
                f.write('END\n')
        f.write('EOF\n')

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Convert verilog to ABEL'
    )

    parser.add_argument('fin', help='Input file')
    parser.add_argument('fout', help='Output file')
    parser.add_argument('--device', default='', help='Device')
    parser.add_argument('--package', default='', help='Package')
    args = parser.parse_args()
    run(args.fin, args.fout, args.device, args.package)

if __name__ == '__main__':
    main()
