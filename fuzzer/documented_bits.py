#!/usr/bin/env python3

# Tobias Senti <git@tsenti.li>
import bitstring
from xcxk import devices

def run(device, package):
    documented_bits = []
    with open(f'./results/{device}{package}/MAGIC_BITSTREAM.txt', 'r') as f:
        for line in f:
            if line == '\n' or line == '':
                continue
            line = line.replace('\n', '')
            (conn, diff) = line.split(':')
            diff = diff.replace(' ', '').replace('[', '').replace(']', '').replace('\'', '').split(',')

            documented_bits.append((int(diff[0]), diff[1]))

    frames = {}
    for (frame_num, diff) in documented_bits:
        diff_bits = bitstring.BitArray('0b' + diff)
        if frame_num not in frames:
            frames[frame_num] = diff_bits
        else:
            frames[frame_num] = diff_bits | frames[frame_num]

    bit_count = 0
    for frame in sorted(frames.keys()):
        bit_count += frames[frame].count(1)
        print(f'{frame:3}: {frames[frame].bin}')

    print('Documented bits:', bit_count)
    total_count = devices.get_dev_num_frames(device) * devices.get_dev_frame_bits(device)
    print(f'Total bits: {total_count}, {bit_count / total_count * 100:.2f}% documented')

def main():
    import argparse

    arg_parser = argparse.ArgumentParser(
        description=
        'Print which bits have been documented/fuzzed for a given device and package'
    )

    arg_parser.add_argument('--device', default='', help='Device')
    arg_parser.add_argument('--package', default='', help='Package')
    args = arg_parser.parse_args()

    run(args.device, args.package)

if __name__ == '__main__':
    main()
