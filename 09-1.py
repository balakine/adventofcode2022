#!/usr/bin/env python3

directions = {
    'U': (0, 1),
    'D': (0, -1),
    'R': (1, 0),
    'L': (-1, 0),
}


def solve(file_name):
    path = ''
    coord_h = (0, 0)
    coord_t = (0, 0)
    path_h = [(0, 0)]
    path_t = [(0, 0)]
    for line in open(file_name, 'r'):
        direction, length = line.split()
        path += direction * int(length)
    for m in path:
        coord_h = (coord_h[0] + directions[m][0], coord_h[1] + directions[m][1])
        path_h.append(coord_h)
        if dist(coord_h, coord_t) > 1:
            coord_t = (coord_t[0] + sign(coord_h[0] - coord_t[0]), coord_t[1] + sign(coord_h[1] - coord_t[1]))
            path_t.append(coord_t)
    print(path_t, len(set(path_t)))
    return len(set(path_t))


def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    elif x < 0:
        return -1
    else:
        return None


def dist(a, b):
    a_x, a_y = a
    b_x, b_y = b
    return max(abs(a_x - b_x), abs(a_y - b_y))


if __name__ == "__main__":
    assert solve('09-test.txt') == 13
    assert solve('09.txt') == 6037
