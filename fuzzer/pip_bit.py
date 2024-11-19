
import utils
from xcxk import parser
from xcxk import container

def fuzz_pip_bitstream(device, package, speed, pip_connection, empty_header, empty_frames, empty_footer):
    filename = utils.create_lca('PIP_BIT', device, package, speed, f'NProgram {pip_connection}', True)
    utils.create_bit(filename)

    parsed = parser.Parser(container.getbits(open(f'./designs/{filename}.BIT', 'rb'), 'BIT'), device)

    header = parsed.header()
    frames = parsed.frames_raw()
    footer = parsed.footer()
    
    if header != empty_header:
        print('Header mismatch')
        print(header)
        print(empty_header)
        exit(1)

    if footer != empty_footer:
        print('Footer mismatch')
        print(footer)
        print(empty_footer)
        exit(1)

    if len(frames) != len(empty_frames):
        print('Frames length mismatch')
        print(len(frames))
        print(len(empty_frames))
        exit(1)
      
    differences = []
    for i in range(len(frames)):
        if frames[i] != empty_frames[i]:
            print(f'Frame mismatch {i}')
            print(f'In frame: {frames[i]}')
            print(f'In empty: {empty_frames[i]}')

            frame_diff = frames[i]['payload'] ^ empty_frames[i]['payload']
            bits_in_empty = empty_frames[i]['payload'] & frame_diff
            bits_in_frame = frames[i]['payload'] & frame_diff

            frame_diff = frame_diff.bin
            bits_in_empty = bits_in_empty.bin
            bits_in_frame = bits_in_frame.bin

            print(f'Frame diff:    {frame_diff}')
            print(f'Bits in empty: {bits_in_empty}')
            print(f'Bits in frame: {bits_in_frame}')

            differences.append([i, frame_diff, bits_in_empty, bits_in_frame])
    return differences 
