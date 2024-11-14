# Tobias Senti <git@tsenti.li>

architectures = {
    '3000': {
        'local_wires': [i for i in range(0, 12)],
        'long_wires': [0, 1, 2, 3, 4, 5]
    }
}

def get_dev_local_wires(dev):
    if not is_device_valid(dev):
        return None
    return architectures[devices[dev]['arch']]['local_wires']

def get_dev_long_wires(dev):
    if not is_device_valid(dev):
        return None
    return architectures[devices[dev]['arch']]['long_wires']

devices = {
    '3090': {
        'arch': '3000',
        'rows': 20,
        'cols': 16,
        'max_ios': 144,
        'packages': ['PC84'],
        'num_frames': 373,
        'frame_bits': 172 - 4,
    }
}

def is_device_valid(dev):
    return dev in devices

def is_device_package_valid(dev, package):
    if dev not in devices:
        return False
    if package not in devices[dev]['packages']:
        return False
    return True

def get_device_num_rows(dev):
    if not is_device_valid(dev):
        return None
    return devices[dev]['rows']

def get_device_num_cols(dev):
    if not is_device_valid(dev):
        return None
    return devices[dev]['cols']

def get_abc():
    return ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def get_device_rows(dev):
    abc = get_abc()
    nrows = get_device_num_rows(dev) + 1
    if nrows > len(abc):
        return None
    return abc[:nrows]

def get_device_cols(dev):
    abc = get_abc()
    ncols = get_device_num_cols(dev) + 1
    if ncols > len(abc):
        return None
    return abc[:ncols]

def get_device_iob_names(dev, package):
    if package in ['PC84']:
        if dev in ['3064', '3090', '3195']:
            iob_names = []
            for i in range(1, 85):
                if i in [1, 2, 12, 13, 21, 22, 31, 32, 42, 43, 54, 55, 64, 65, 74]:
                    continue
                iob_names.append(f'P{i}')
            return iob_names
    
    return None

def get_device_pad_names(dev, package):
    if not is_device_valid(dev):
        return None
    return [f'PAD{i}' for i in range(1, devices[dev]['max_ios'] + 1)]

def get_dev_num_frames(dev):
    if not is_device_valid(dev):
        return None
    return devices[dev]['num_frames']

def get_dev_frame_bits(dev):
    if not is_device_valid(dev):
        return None
    return devices[dev]['frame_bits']
