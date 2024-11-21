#!/usr/bin/env python3
# Tobias Senti <git@tsenti.li>

import utils
import pips
import pip_bit
from xcxk import parser
from xcxk import container
from xcxk import devices

def fuzz_iob_local_long_pips_exist(device, package, speed, split_start, split_end, onlyiobmapping):
    pads = devices.get_device_pad_names(device, package)

    split = False
    if split_start != '' and split_end != '':
        if split_start in pads:
            if split_end in pads:
                pads = pads[pads.index(split_start):pads.index(split_end)+1]
            else:
                pads = pads[pads.index(split_start):]
            split = True
        else:
            print('Invalid split range')
            exit(1)

    pips_filename = f'./results/{device}/IOB_LOCAL_LONG_PIPS'
    map_filename = f'./results/{device}/package/{package}_IOB_MAPPING'
    if split:
        pips_filename += f'_{split_start}_to_{split_end}'
        map_filename += f'_{split_start}_to_{split_end}'

    if not onlyiobmapping:
        with open(pips_filename + '.txt', 'w') as f:
            with open(map_filename + '.txt', 'w') as map:
                for pad in pads:
                    for pin in ['I', 'O', 'T', 'Q', 'IK', 'OK']:
                        (pip_names, log) = pips.find_local_long_pips_for_block(device, package, speed, pad, pin, True)
                        
                        # Write pips
                        if not onlyiobmapping:
                            for pip in pip_names:
                                f.write(f'{pad}.{pin} {pip}\n')
                            f.write('\n')
                            f.flush()

                        # Write mapping
                        if pin == 'I':
                            iob_name = ''
                            if 'Fixing unconnected pin P' in log:
                                iob_name = 'P' + log.split('Fixing unconnected pin P')[1].split('.')[0]
                            elif 'Fixing unconnected pin U' in log:
                                iob_name = 'U' + log.split('Fixing unconnected pin U')[1].split('.')[0]
                            else:
                                print(f'Error: Could not find IOB name for {pad}')
                                exit(1)
                            
                            map.write(f'{iob_name} {pad}\n')
                            map.flush()

                    f.write('\n')
    else:
        with open(map_filename + '.txt', 'w') as map:
            for pad in pads:
                for pin in ['I']:
                    (pip_names, log) = pips.find_local_long_pips_for_block(device, package, speed, pad, pin, True)
                    
                    # Write pips
                    if not onlyiobmapping:
                        for pip in pip_names:
                            f.write(f'{pad}.{pin} {pip}\n')
                        f.write('\n')
                        f.flush()

                    # Write mapping
                    if pin == 'I':
                        iob_name = ''
                        if 'Fixing unconnected pin P' in log:
                            iob_name = 'P' + log.split('Fixing unconnected pin P')[1].split('.')[0]
                        elif 'Fixing unconnected pin U' in log:
                            iob_name = 'U' + log.split('Fixing unconnected pin U')[1].split('.')[0]
                        else:
                            print(f'Error: Could not find IOB name for {pad}')
                            exit(1)
                        
                        map.write(f'{iob_name} {pad}\n')
                        map.flush()


def fuzz_iob_direct_exist(device, package, speed, split_start, split_end):
    pads = devices.get_device_pad_names(device, package)
    rows = devices.get_device_rows(device)[:-1]
    perimeter_rows = [rows[0], rows[-1]]
    cols = devices.get_device_cols(device)[:-1]
    perimeter_cols = [cols[0], cols[-1]]

    split = False
    if split_start != '' and split_end != '':
        if split_start in pads:
            if split_end in pads:
                pads = pads[pads.index(split_start):pads.index(split_end)+1]
            else:
                pads = pads[pads.index(split_start):]
            split = True
        else:
            print('Invalid split range')
            exit(1)

    pips_filename = f'./results/{device}/IOB_DIRECT'
    if split:
        pips_filename += f'_{split_start}_to_{split_end}'
    with open(pips_filename + '.txt', 'w') as f:
        for pad in pads:
            lca = ''
            pip_names = []
            for pin in ['I', 'Q', 'O', 'T']:
                for clb_pin in ['A', 'B', 'C', 'D', 'E', 'DI', 'EC', 'RD', 'K'] if pin in ['I', 'Q'] else ['X', 'Y']:
                    for row in perimeter_rows:
                        for col in cols:
                            pip_name = f'{row}{col}.{clb_pin}:{pad}.{pin}'
                            if pip_name not in pip_names:
                                pip_names.append(pip_name)
                                lca += f'NProgram {pip_name}\n'
                    for row in rows:
                        for col in perimeter_cols:
                            pip_name = f'{row}{col}.{clb_pin}:{pad}.{pin}'
                            if pip_name not in pip_names:
                                pip_names.append(pip_name)
                                lca += f'NProgram {pip_name}\n'

            filename = f'{pad}_IOB'
            filename = utils.create_lca(filename, device, package, speed, lca, True)
            log = utils.create_bit(filename)

            empty = True
            for pip_name in pip_names:
                if f'`{pip_name}\' is not programmable.' not in log:
                    name = pip_name.split(':')[1]
                    f.write(f'{name} {pip_name}\n')
                    f.flush()
                    empty = False
            if not empty:
                f.write('\n')
            f.flush()

def fuzz_clb_direct_exist(device, package, speed, split_start, split_end):
    rows = devices.get_device_rows(device)[:-1]
    cols = devices.get_device_cols(device)[:-1]

    all_rows = rows.copy()

    split = False
    if split_start != '' and split_end != '':
        if split_start in rows and split_end in rows:
            rows = rows[rows.index(split_start):rows.index(split_end)+1]
            split = True
        else:
            print('Invalid split range')
            exit(1)

    pips_filename = f'./results/{device}/CLB_DIRECT'
    if split:
        pips_filename += f'_{split_start}_to_{split_end}'

    with open(pips_filename + '.txt', 'w') as f:
        for r_idx, row in enumerate(all_rows):
            if row not in rows:
                continue
            for c_idx, col in enumerate(cols):
                lca = ''
                pip_names = []
                for out in ['X', 'Y']:
                    for inp in ['A', 'B', 'C', 'D', 'E', 'DI', 'EC', 'RD', 'K']:
                        if r_idx > 0:
                            pip_name = f'{row}{col}.{out}:{all_rows[r_idx-1]}{col}.{inp}'
                            if pip_name not in pip_names:
                                pip_names.append(pip_name)
                                lca += f'NProgram {pip_name}\n'
                        if r_idx < len(all_rows)-1:
                            pip_name = f'{row}{col}.{out}:{all_rows[r_idx+1]}{col}.{inp}'
                            if pip_name not in pip_names:
                                pip_names.append(pip_name)
                                lca += f'NProgram {pip_name}\n'

                        if c_idx > 0:
                            pip_name = f'{row}{col}.{out}:{row}{cols[c_idx-1]}.{inp}'
                            if pip_name not in pip_names:
                                pip_names.append(pip_name)
                                lca += f'NProgram {pip_name}\n'
                        if c_idx < len(cols)-1:
                            pip_name = f'{row}{col}.{out}:{row}{cols[c_idx+1]}.{inp}'
                            if pip_name not in pip_names:
                                pip_names.append(pip_name)
                                lca += f'NProgram {pip_name}\n'

                filename = f'{row}{col}_DIR'
                filename = utils.create_lca(filename, device, package, speed, lca, True)
                log = utils.create_bit(filename)

                empty = True
                for pip_name in pip_names:
                    if f'`{pip_name}\' is not programmable.' not in log:
                        name = pip_name.split(':')[0]
                        f.write(f'{name} {pip_name}\n')
                        f.flush()
                        empty = False
                if not empty:
                    f.write('\n')
                f.flush()

def fuzz_clb_local_long_pips_exist(device, package, speed, split_start, split_end):
    rows = devices.get_device_rows(device)[:-1]
    cols = devices.get_device_cols(device)[:-1]
    filename = f'./results/{device}/CLB_LOCAL_LONG_PIPS'

    if split_start != '' and split_end != '':
        if split_start in rows and split_end in rows:
            rows = rows[rows.index(split_start):rows.index(split_end)+1]
            filename += f'_{split_start}_to_{split_end}'
        else:
            print('Invalid split range')
            exit(1)

    with open(filename + '.txt', 'w') as f:
        for row in rows:
            for col in cols:
                for pin in ['A', 'B', 'C', 'D', 'E', 'DI', 'EC', 'RD', 'K', 'X', 'Y']:
                    name = f'{row}{col}'
                    (pip_names, log) = pips.find_local_long_pips_for_block(device, package, speed, name, pin, True)
                    for pip in pip_names:
                        f.write(f'{name}.{pin} {pip}\n')
                    f.write('\n')
                    f.flush()
                f.write('\n')

def fuzz_local_long_pips_exist(device, package, speed, split_start, split_end):
    rows = devices.get_device_rows(device)
    filename = f'./results/{device}/LOCAL_LONG_PIPS'

    if split_start != '' and split_end != '':
        if split_start in rows and split_end in rows:
            rows = rows[rows.index(split_start):rows.index(split_end)+1]
            filename += f'_{split_start}_to_{split_end}'
        else:
            print('Invalid split range')
            exit(1)

    with open(filename + '.txt', 'w') as f:
        for row in rows:
            (pip_names, log) = pips.find_local_long_pips(device, package, speed, row)
            for pip in pip_names:
                f.write(f'{pip}\n')
            f.write('\n\n')
            f.flush()

def fuzz_magic_connections(device, package, speed, split_start, split_end):
    rows = devices.get_device_rows(device)
    cols = devices.get_device_cols(device)
    filename = f'./results/{device}/MAGIC_CONNECTIONS'

    if split_start != '' and split_end != '':
        if split_start in rows and split_end in rows:
            rows = rows[rows.index(split_start):rows.index(split_end)+1]
            filename += f'_{split_start}_to_{split_end}'
        else:
            print('Invalid split range')
            exit(1)

    with open(filename + '.txt', 'w') as f:
        for row in rows:
            for col in cols:
                lca = ''
                name = f'{row}{col}.20.1.'

                conn_name = []
                for start in range(0, 20):
                    for end in range(0, 20):
                        if start == end:
                            continue
                        lca += f'NProgram {name}{start} {name}{end}\n'
                        conn_name.append((start, end))

                filename = f'{row}{col}_MAG'
                filename = utils.create_lca(filename, device, package, speed, lca, True)
                log = utils.create_bit(filename)
                print(log)

                for (start, end) in conn_name:
                    if f'Pin {start+1} and {end+1}: Unconnectable.' not in log:
                        if f'`{name}{start}\' is not programmable.' not in log and f'`{name}{end}\' is not programmable.' not in log:
                            print(f'{name}{start} {name}{end}')
                            f.write(f'{name}{start} {name}{end}\n')
                            f.flush()
                f.write('\n')

def fuzz_magic_connections_bitstream(device, package, speed, split_start, split_end, empty_header, empty_frames, empty_footer):
    with open(f'./results/{device}/MAGIC_CONNECTIONS.txt', 'r') as f:
        filename = f'./results/{device}/MAGIC_BITSTREAM'

        rows = devices.get_device_rows(device)[:-1]
        if split_start != '' and split_end != '':
            if split_start in rows and split_end in rows:
                rows = rows[rows.index(split_start):rows.index(split_end)+1]
                filename += f'_{split_start}_to_{split_end}'
            else:
                print('Invalid split range')
                exit(1)

        with open(f'{filename}.txt', 'w') as diff:
            for line in f:
                if line == '\n' or line == '':
                    continue
                (start, end) = line.strip().split(' ')
                if start[0] not in rows:
                    continue

                differences = pip_bit.fuzz_pip_bitstream(device, package, speed, f'{start} {end}', empty_header, empty_frames, empty_footer)
                if len(differences) == 0:
                    diff.write(f'{start} {end}:[]\n')
                    print(f'{start} {end} has no differences')
                elif len(differences) == 1:
                    print(f'{start} {end}: {differences[0]}')
                    diff.write(f'{start} {end}:{differences[0]}\n')
                else:
                    print(f'{start} {end} has multiple differences')
                    print(differences)
                    diff.write(f'{start} {end}:{differences}\n')
                    diff.write('multiple differences\n')
                    exit(1)
                diff.flush()

def main():
    import argparse

    arg_parser = argparse.ArgumentParser(description='Fuzz')
    arg_parser.add_argument('--device', default='', help='Device')
    arg_parser.add_argument('--package', default='', help='Package')
    arg_parser.add_argument('--speed', default='', help='Speed')
    arg_parser.add_argument('--target', default='iob-config', help='Target')
    arg_parser.add_argument('--split_start', default='', help='Split the fuzz job')
    arg_parser.add_argument('--split_end', default='', help='Split the fuzz job')
    arg_parser.add_argument('--onlyiobmapping', default=False, action='store_true', help='Only generate IOB mapping')

    args = arg_parser.parse_args()
    device = args.device
    package = args.package
    speed = args.speed
    split_start = args.split_start
    split_end = args.split_end

    if not devices.is_device_package_valid(device, package):
        print('Invalid device/package')
        exit(1)

    if args.target == 'iob-local-long-pips':
        fuzz_iob_local_long_pips_exist(device, package, speed, split_start, split_end, args.onlyiobmapping)
        exit(1)

    if args.target == 'clb-local-long-pips':
        fuzz_clb_local_long_pips_exist(device, package, speed, split_start, split_end)
        exit(1)

    if args.target == 'magic-connections':
        fuzz_magic_connections(device, package, speed, split_start, split_end)
        exit(1)
    
    if args.target == 'local-long-pips':
        fuzz_local_long_pips_exist(device, package, speed, split_start, split_end)
        exit(1)

    if args.target == 'iob-direct-pips':
        fuzz_iob_direct_exist(device, package, speed, split_start, split_end)
        exit(1)

    if args.target == 'clb-direct-pips':
        fuzz_clb_direct_exist(device, package, speed, split_start, split_end)
        exit(1)

    print('Creating empty bitstream')
    emptyfilename = utils.create_lca('EMPTY', device, package, speed, '', True)
    utils.create_bit(emptyfilename)

    parsed_empty = parser.Parser(container.getbits(open(f'./designs/{emptyfilename}.BIT', 'rb'), 'BIT'), device)

    empty_header = parsed_empty.header()
    empty_frames = parsed_empty.frames_raw()
    empty_footer = parsed_empty.footer()

    if args.target == 'magic-bitstream':
        fuzz_magic_connections_bitstream(device, package, speed, split_start, split_end, empty_header, empty_frames, empty_footer)
        exit(1)

    print('Invalid target')

if __name__ == "__main__":
    main();
