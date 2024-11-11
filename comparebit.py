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

from xc2k import parser
from xc2k import container

def print_header(header):
    print('header')
    print('  pad1: %d bytes (min: 4)' % len(header['pad1']))
    print('  preamble: %d' % header['preamble'])
    print('  length: %d' % header['length'])
    print('  pad2: %d bytes (min: 4)' % len(header['pad2']))

def print_frame(frame, id):
    print(f'frame{id}: {frame["payload"]}')

def run(file1, file2, format):
    pfile1 = parser.Parser(container.getbits(file1, format))
    pfile2 = parser.Parser(container.getbits(file2, format))

    header1 = pfile1.header()
    header2 = pfile2.header()

    if header1 != header2:
        print('Header mismatch')
        print('File1:')
        print_header(header1)
        print('File2:')
        print_header(header2)
    else:
        print('Headers match')
        print_header(header1)
    
    frames1 = pfile1.frames_raw()
    frames2 = pfile2.frames_raw()

    assert len(frames1) == len(frames2)

    for i in range(len(frames1)):
        frame1 = frames1[i]
        frame2 = frames2[i]

        if frame1 != frame2:
            print(f'Frame {i} mismatch')
            p1 = frame1['payload']
            p2 = frame2['payload']
            print(f"Diff:   {p1 ^ p2}")
            print_frame(frame1, 1)
            print_frame(frame2, 2)

    footer1 = pfile1.footer()
    footer2 = pfile2.footer()

    if footer1 != footer2:
        print('Footer mismatch')
        print('File1:')
        print('footer: %d bytes (min: 4)' % len(footer1['postamble']))
        print('File2:')
        print('footer: %d bytes (min: 4)' % len(footer2['postamble']))
    else:
        print('footer: %d bytes (min: 4)' % len(footer1['postamble']))

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description=
        'Compare two bitstreams'
    )

    parser.add_argument('--verbose', type=int, help='')
    parser.add_argument('--format', default='BIT', help='One of: bin, bit, rom')
    parser.add_argument('file1', help='Input file')
    parser.add_argument('file2', help='Input file')
    args = parser.parse_args()
    run(open(args.file1, 'rb'), open(args.file2, 'rb'), format=args.format)

if __name__ == '__main__':
    main()

