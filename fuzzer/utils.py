# Tobias Senti <git@tsenti.li>

from xcxk import xact
import os
import random

def create_lca(filename, device, package, speed, lca_content, unique = False):
    filename = filename[:7]
    if unique:
        while os.path.exists('./designs/' + filename + '.LCA'):
            filename = 'P' + str(random.randint(0, 999999))

    with open('./designs/' + filename + '.LCA', 'w') as f:
        f.write('Version 2\n')
        f.write(f'Design {device}{package}\n')
        f.write(f'Speed {speed}\n\n')
        f.write(lca_content)
    
    return filename

def create_bit(filename):
    log = xact.lca2bit("./designs", filename)
    print(log)
    return log

def build_blk(location, name, base_type, config):
    blk = f'Nameblk {location} {name}\n'
    blk += f'Editblk {location}\n'
    blk += f'Base {base_type}\n'
    if config is not None and len(config) > 0:
        blk += f'Config'
        for key in config.keys():
            blk += f' {key}:'
            for idx, value in enumerate(config[key]):
                if value == '':
                    continue
                blk += f'{value}'
                if idx < len(config[key]) - 1:
                    blk += ':'
        blk += '\n'
    blk += 'Endblk\n'
    return blk

def recursve_choice(cfg):
    if len(cfg) == 0:
        return None

    print('Choice: ', cfg)

    child_result = recursve_choice(cfg[1:])
    print(f'Child result for {cfg[0]}: {child_result}')

    result = []
    if type(cfg[0]) is not list:
        if type(child_result) is list:
            print('notlist, list')
            for cr in child_result:
                tmp = [cfg[0]]
                tmp.extend(cr)
                result.append(tmp)
        else:
            print('notlist, notlist')
            tmp = [cfg[0]]
            if child_result != None:
                print('notlist, notlist, notnone')
                tmp.append(child_result)
            result.append(tmp)
    else:
        for opt in cfg[0]:
            if type(child_result) is list:
                for cr in child_result:
                    tmp = [opt]
                    tmp.extend(cr)
                    result.append(tmp)
            else:
                tmp = [opt]
                if child_result != None:
                    tmp.append(child_result)
                result.append(tmp)

    print(f'Result for {cfg[0]}: {result}')
    return result

def build_possible_configs(options, modifiers = []):
    configs = []
    different_options = 2**len(options)
    # Build possible combinations of options
    for i in range(different_options):
        config = []
        for j in range(len(options)):
            if i & (1 << j):
                opt = options[j]
                config.append(options[j])
        configs.append(config)

    print('Preliminary configs: ', configs)
    final_configs = []
    for cfg in configs:
        print('\nCFG: ', cfg)
        res = recursve_choice(cfg)
        if res != None:
            final_configs.extend(res)

    return final_configs
