#!/usr/bin/env python3

# Tobias Senti <git@tsenti.li>

def read_lca(fin):
    routes = []
    with open(fin, 'r') as f:
        lines = f.readlines()
        nets = []
        for line in lines:
            if line.startswith('Addnet '):
                nets.append(line.replace('\n', '').split(' ')[1])
            if line.startswith('NProgram '):
                pips = line.replace('\n', '').split(' ')[1:]
                print(f'{pips}')

                route = []
                i = 0
                while i < len(pips):
                    if pips[i] not in nets and pips[i] != '':
                        if ':' in pips[i]:
                            route.append(pips[i])
                            print(f'Pip: {pips[i]}')
                        else:
                            if i+1 >= len(pips):
                                print(f'Invalid pip: {pips[i]} {len(pips)} {i}')
                                exit(1)
                            new_pip = f'{pips[i]} {pips[i+1]}'
                            print(f'New pip: {new_pip}')
                            route.append(new_pip)
                            i += 1
                    else:
                        print(f'Net: {pips[i]}')
                    i += 1

                routes.append(route)

    for route in routes:
        for pip in route:
            if ':' not in pip and ' ' not in pip:
                print(f'Invalid pip: {pip}')
                exit(1)

    # Remove -l and -s from pips
    for route in routes:
        for i in range(len(route)):
            if '-l' in route[i]:
                route[i] = route[i].replace('-l', '')
            if '-s' in route[i]:
                route[i] = route[i].replace('-s', '')

    return routes

def run(fin, device, package):
    routes = read_lca(fin)
    print(f'Found {len(routes)} routes')

    magic_connections = []
    with open(f'./results/{device}/MAGIC_CONNECTIONS.txt', 'r') as f:
        for line in f:
            if line == '\n' or line == '':
                continue
            magic_connections.append(line.replace('\n', ''))

    clb_local_long_pips = []
    with open(f'./results/{device}/CLB_LOCAL_LONG_PIPS.txt', 'r') as f:
        for line in f:
            if line == '\n' or line == '':
                continue
            clb_local_long_pips.append(line.replace('\n', '').split(' ')[1])

    iob_local_long_pips = []
    with open(f'./results/{device}/IOB_LOCAL_LONG_PIPS.txt', 'r') as f:
        for line in f:
            if line == '\n' or line == '':
                continue
            iob_local_long_pips.append(line.replace('\n', '').split(' ')[1])

    pips = []
    with open(f'./results/{device}/LOCAL_LONG_PIPS.txt', 'r') as f:
        for line in f:
            if line == '\n' or line == '':
                continue
            pips.append(line.replace('\n', ''))

    clb_direct = []
    with open(f'./results/{device}/CLB_DIRECT.txt', 'r') as f:
        for line in f:
            if line == '\n' or line == '':
                continue
            pip = line.replace('\n', '').split(' ')[1].split(':')
            # Add both variants
            clb_direct.append(pip[0] + ':' + pip[1])
            clb_direct.append(pip[1] + ':' + pip[0])

    iob_direct = []
    with open(f'./results/{device}/IOB_DIRECT.txt', 'r') as f:
        for line in f:
            if line == '\n' or line == '':
                continue
            pip = line.replace('\n', '').split(' ')[1].split(':')
            # Add both variants
            iob_direct.append(pip[0] + ':' + pip[1])
            iob_direct.append(pip[1] + ':' + pip[0])

    for route in routes:
        for conn in route:
            if conn not in magic_connections\
            and conn not in clb_local_long_pips\
            and conn not in iob_local_long_pips\
            and conn not in pips\
            and conn not in clb_direct\
            and conn not in iob_direct:
                print(f'Unknown connection: {conn}')

def main():
    import argparse

    arg_parser = argparse.ArgumentParser(
        description=
        'Dump bitstream info'
    )

    arg_parser.add_argument('fin', help='.LCA input file')
    arg_parser.add_argument('--device', default='', help='Device')
    arg_parser.add_argument('--package', default='', help='Package')
    args = arg_parser.parse_args()

    run(args.fin, args.device, args.package)

if __name__ == '__main__':
    main()