#!/usr/bin/env python3
# Tobias Senti <git@tsenti.li>

import utils
import blk_pips
import pip_bit
from xcxk import parser
from xcxk import container
from xcxk import devices

def fuzz_iob_local_long_pips_exist(device, package, speed, split_start, split_end):
    pads = devices.get_device_pad_names(device, package)

    split = False
    if split_start in pads and split_end in pads:
        pads = pads[pads.index(split_start):pads.index(split_end)+1]
        split = True

    pips_filename = f'./results/{device}{package}_IOB_LOCAL_LONG_PIPS'
    map_filename = f'./results/{device}{package}_IOB_MAPPING'
    if split:
        pips_filename += f'_{split_start}_to_{split_end}'
        map_filename += f'_{split_start}_to_{split_end}'
    with open(pips_filename + '.txt', 'w') as f:
        with open(map_filename + '.txt', 'w') as map:
            for pad in pads:
                for pin in ['I', 'O', 'T', 'Q', 'IK', 'OK']:
                    (pips, log) = blk_pips.find_local_long_pips_for_block(device, package, speed, pad, pin, True)
                    
                    # Write pips
                    for pip in pips:
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

def fuzz_clb_local_long_pips_exist(device, package, speed, split_start, split_end):
    rows = devices.get_device_rows(device)[:-1]
    cols = devices.get_device_cols(device)[:-1]
    filename = f'./results/{device}{package}_CLB_LOCAL_LONG_PIPS'

    if split_start in rows and split_end in rows:
        rows = rows[rows.index(split_start):rows.index(split_end)+1]
        filename += f'_{split_start}_to_{split_end}'

    with open(filename + '.txt', 'w') as f:
        for row in rows:
            for col in cols:
                for pin in ['A', 'B', 'C', 'D', 'E', 'DI', 'EC', 'RD', 'K', 'X', 'Y']:
                    name = f'{row}{col}'
                    (pips, log) = blk_pips.find_local_long_pips_for_block(device, package, speed, name, pin, True)
                    for pip in pips:
                        f.write(f'{name}.{pin} {pip}\n')
                    f.write('\n')
                    f.flush()
                f.write('\n')

def fuzz_magic_connections(device, package, speed, split_start, split_end):
    rows = devices.get_device_rows(device)[:-1]
    cols = devices.get_device_cols(device)[:-1]
    filename = f'./results/{device}{package}_MAGIC_CONNECTIONS'

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
    with open(f'./results/{device}{package}_MAGIC_CONNECTIONS.txt', 'r') as f:
        filename = f'./results/{device}{package}_MAGIC_BITSTREAM'

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
                    diff.write(f'{start} {end}:{differences[0]}\n')
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
        fuzz_iob_local_long_pips_exist(device, package, speed, split_start, split_end)
        exit(1)

    if args.target == 'clb-local-long-pips':
        fuzz_clb_local_long_pips_exist(device, package, speed, split_start, split_end)
        exit(1)

    if args.target == 'magic-connections':
        fuzz_magic_connections(device, package, speed, split_start, split_end)
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
