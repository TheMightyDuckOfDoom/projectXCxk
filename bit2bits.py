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

'''
Inspired by the .bits format from project x-ray
Unlike 7 series though, there are a lot of 1's in unused logic
'''

from fuzzer.xcxk.bit2bits import bit2bitsf

def run(fin, fout, format):
    bit2bitsf(fin, fout, format)

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description=
        'Create a .bits file, a text equivalent representation of the bitstream'
    )

    parser.add_argument('--verbose', type=int, help='')
    parser.add_argument('--format', default='BIT', help='One of: bin, bit, rom')
    parser.add_argument('fin', nargs='?', default='/dev/stdin', help='Input file')
    parser.add_argument('fout', nargs='?', default='/dev/stdout', help='Output file')
    args = parser.parse_args()
    run(open(args.fin, 'rb',), open(args.fout, 'w'), format=args.format)

if __name__ == '__main__':
    main()
