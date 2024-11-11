# Tobias Senti <git@tsenti.li>

# IOB config
# I:{PAD,Q}
# BUF:{,ON,TRI}

from xc2k import parser
from xc2k import container
import utils
from bitstring import Bits

def fuzz(device, package, speed, empty_header, empty_frames, empty_footer):
    if package != 'PC68':
        print("Error: Invalid package")
        exit(1)

    IOB_NAMES = []
    if package == 'PC68':
        for i in range(1, 69):
            if i in {1, 10, 18, 25, 26, 35, 44, 45, 52, 60}:
                continue
            IOB_NAMES.append(f'P{i}')
    
    IOB_I_CONFIG = ['PAD', 'Q']
    IOB_BUF_CONFIG = ['', 'ON', 'TRI']

    differences = {}
    config_bitpos = {}

    for iob in IOB_NAMES:
        differences[iob] = {}
        for i_config in IOB_I_CONFIG:
            differences[iob][i_config] = {}
            for buf_config in IOB_BUF_CONFIG:
                differences[iob][i_config][buf_config] = []
                print(f'\n\nFuzzing IOB {iob} I:{i_config} BUF:{buf_config}')
                lca = f'Nameblk {iob} {iob}IOB\n'
                lca += f'Editblk {iob}\n'
                lca += 'Base IO\n'
                lca += f'Config I:{i_config} BUF:{buf_config}\n'
                lca += 'Endblk\n'

                utils.create_lca(f'./designs/IOB.lca', device, package, speed, lca)
                utils.create_bit(f'IOB')

                parsed = parser.Parser(container.getbits(open(f'./designs/IOB.BIT', 'rb'), 'BIT'), device)
                header = parsed.header()
                frames = parsed.frames_raw()
                footer = parsed.footer()

                if header != empty_header:
                    print(f'Header mismatch for IOB')
                    print(f'Empty header: {empty_header}')
                    print(f'Header: {header}')
                    exit(1)
                if footer != empty_footer:
                    print(f'Footer mismatch for IOB')
                    print(f'Empty footer: {empty_footer}')
                    print(f'Footer: {footer}')
                    exit(1)

                if len(frames) != len(empty_frames):
                    print(f'Frame count mismatch for IOB')
                    print(f'Empty frame count: {len(empty_frames)}')
                    print(f'Frame count: {len(frames)}')
                    exit(1)

                # Find differences in frames
                for i in range(len(frames)):
                    if frames[i] != empty_frames[i]:
                        print(f'Frame {i} mismatch for IOB')
                        empty_frame = empty_frames[i]['payload']
                        frame = frames[i]['payload']
                        diff = empty_frame ^ frame

                        in_empty = empty_frame & diff
                        in_frame = frame & diff

                        differences[iob][i_config][buf_config].append({
                            'frame': i,
                            'diff': diff,
                            'in_empty': in_empty,
                            'in_frame': in_frame
                        })

                        print(f'Bits different: {diff}')
                        print(f'Bits in empty: {in_empty}')
                        print(f'Bits in frame: {in_frame}')
                
                if len(differences[iob][i_config][buf_config]) > 2:
                    print(f'More than 2 differences for IOB {iob} I:{i_config} BUF:{buf_config}')

        # Find configuration with the least differences
        empty_cfg = None
        max_diff = 1000000

        for i_config in IOB_I_CONFIG:
            for buf_config in IOB_BUF_CONFIG:
                if len(differences[iob][i_config][buf_config]) == 0:
                    if empty_cfg is None:
                        empty_cfg = (i_config, buf_config)
                    else:
                        print('Multiple configurations with no differences')
                        exit(1)
        if empty_cfg is None:
            print('No configuration with no differences')
            exit(1) 

        print('IOB config used in empty bitstream:', empty_cfg)


        # Find config bits
        config_bitpos[iob] = {}
        for i_config in IOB_I_CONFIG:
            for buf_config in IOB_BUF_CONFIG:
                if i_config != empty_cfg[0] and buf_config != empty_cfg[1]:
                    # Config that is completely different from the empty bitstream
                    continue
                if i_config == empty_cfg[0] and buf_config == empty_cfg[1]:
                    # Config that is the same as the empty bitstream
                    continue
                
                # Find which bit is different
                diffs = differences[iob][i_config][buf_config]

                if len(diffs) == 0:
                    print(f'No differences for IOB {iob} I:{i_config} BUF:{buf_config} compared to empty bitstream, but there should be')
                    exit(1)

                if len(diffs) > 1: 
                    print(f'Multiple differences for IOB {iob} I:{i_config} BUF:{buf_config} compared to empty bitstream, but there should be only one')

                for diff in diffs:
                    frame = diff['frame']
                    bit_pos = Bits(diff['diff']).find('0b1')[0]
                    in_empty = diff['in_empty']
                    in_frame = diff['in_frame']

                    print('Config %s %s has difference in frame %d at bit %d: %s' % (i_config, buf_config, frame, bit_pos, in_frame))

                    diff_config = i_config if i_config != empty_cfg[0] else buf_config

                    if diff_config not in config_bitpos[iob]:
                        config_bitpos[iob][diff_config] = []
                    config_bitpos[iob][diff_config].append({
                        'frame': frame,
                        'bit_pos': bit_pos,
                        'value': in_frame
                    })

    with open(f'./results/XC{device}{package}_IOB.txt', 'w') as f:
        for iob in IOB_NAMES:
            if iob not in config_bitpos:
                continue
            for config in config_bitpos[iob]:
                diffs = config_bitpos[iob][config]
                for d in diffs:
                    f.write(f'{iob} {config} frame {d["frame"]} bit {d["bit_pos"]}: {d["value"]}\n')
            f.write('\n')

    print('Done fuzzing IOBs')
