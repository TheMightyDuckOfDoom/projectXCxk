#!/usr/bin/env python3
# Tobias Senti <git@tsenti.li>

import utils
import iob
from xc2k import parser
from xc2k import container

def main():
    import argparse

    arg_parser = argparse.ArgumentParser(description='Fuzz')
    arg_parser.add_argument('--device', default='2064', help='Device')
    arg_parser.add_argument('--package', default='PC68', help='Package')
    arg_parser.add_argument('--speed', default='-70', help='Speed')

    args = arg_parser.parse_args()
    device = args.device
    package = args.package
    speed = args.speed

    print('Creating empty bitstream')
    utils.create_lca('./designs/EMPTY.lca', device, package, speed, '')
    utils.create_bit('EMPTY')

    parsed_empty = parser.Parser(container.getbits(open('./designs/EMPTY.BIT', 'rb'), 'BIT'), device)

    empty_header = parsed_empty.header()
    empty_frames = parsed_empty.frames_raw()
    empty_footer = parsed_empty.footer()

    print('Fuzzing IOBs')
    iob.fuzz(device, package, speed, empty_header, empty_frames, empty_footer)

if __name__ == "__main__":
    main();