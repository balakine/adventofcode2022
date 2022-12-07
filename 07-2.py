#!/usr/bin/env python3

def solve(file_name):
    t = [{'type': 'd', 'name': '/', 'size': 0, 'parent': None}]
    current_dir = 0
    for line in open(file_name, 'r'):
        if line.startswith('$ cd '):
            _, _, dir_name = line.split()
            if dir_name == '/':
                current_dir = 0
            elif dir_name == '..':
                current_dir = t[current_dir]['parent']
            else:
                current_dir = next(i for i, x in enumerate(t) if x['name'] == dir_name and x['parent'] == current_dir)
        elif line.startswith('$ ls'):
            pass
        else:
            op1, name = line.split()
            if op1 == 'dir':
                node_type = 'd'
                size = 0
            else:
                node_type = 'f'
                size = int(op1)
            t.append({'type': node_type, 'name': name, 'size': size, 'parent': current_dir})
            # Add file size to all parent directories
            if node_type == 'f':
                p = current_dir
                while p is not None:
                    t[p]['size'] += size
                    p = t[p]['parent']
    free_space = 70_000_000 - t[0]['size']
    space_needed = 30_000_000 - free_space
    candidate = 0
    for i in range(len(t)):
        if t[i]['type'] == 'd' and space_needed < t[i]['size'] < t[candidate]['size']:
            candidate = i
    print(t[candidate]['size'])
    return t[candidate]['size']


if __name__ == "__main__":
    assert solve('07-test.txt') == 24933642
    assert solve('07.txt') == 214171
