#!/usr/bin/env python3

# Tobias Senti <git@tsenti.li>

from xc2k import xact

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description=
        'Dump bitstream info'
    )

    parser.add_argument('design', help='Design file name inside /designs')
    args = parser.parse_args()

    log = xact.lca2bit("./designs", args.design)
    print(log)

if __name__ == '__main__':
    main()