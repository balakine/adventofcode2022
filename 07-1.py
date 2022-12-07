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
    s = sum(x['size'] for x in t if x['type'] == 'd' and x['size'] <= 100000)
    print(s)
    return s


if __name__ == "__main__":
    assert solve('07-test.txt') == 95437
    solve('07.txt')
