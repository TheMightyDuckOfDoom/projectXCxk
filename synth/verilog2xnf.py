#!/usr/bin/env python3

# Tobias Senti <git@tsenti.li>

from pyverilog.vparser.parser import parse

def run(file):
    ast, directives = parse(file)

    ast.show()
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
    for item in top_module.items:
        if type(item).__name__ == 'Decl':
            for decl in item.list:
                if type(decl).__name__ == 'Input':
                    inputs.append(decl.name)
                elif type(decl).__name__ == 'Output':
                    outputs.append(decl.name)
                elif type(decl).__name__ == 'Wire':
                    wires.append(decl.name)

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Convert verilog to ABEL'
    )

    parser.add_argument('fin', help='Input file')
    args = parser.parse_args()
    run(open(args.fin, 'r'))

if __name__ == '__main__':
    main()
