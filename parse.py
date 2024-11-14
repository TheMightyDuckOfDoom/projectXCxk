#!/usr/bin/env python3

# Copyright (C) 2018  John McMaster <JohnDMcMaster@gmail.com>
# https://github.com/JohnDMcMaster/project2064
  
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
  
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from fuzzer.xcxk import parser
from fuzzer.xcxk import container

def run(f, format, dev):
    p = parser.Parser(container.getbits(f, format), dev)

    header = p.header()

    print('header')
    print('  pad1: %d bits (min: 4)' % len(header['pad1']))
    print('  preamble: %d' % header['preamble'])
    print('  length: %d' % header['length'])
    print('  pad2: %d bits (min: 4)' % len(header['pad2']))

    for frame in p.frames_raw():
        print('frame: %s' % frame['payload'])
    footer = p.footer()
    print('footer: %d bits (min: 4)' % len(footer['postamble']))

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description=
        'Dump bitstream info'
    )

    parser.add_argument('--verbose', type=int, help='')
    parser.add_argument('--format', default='BIT', help='One of: bin, bit, rom')
    parser.add_argument('--device', default='', help='Device')
    parser.add_argument('fin', help='Input file')
    args = parser.parse_args()
    run(open(args.fin, 'rb'), format=args.format, dev=args.device)

if __name__ == '__main__':
    main()
