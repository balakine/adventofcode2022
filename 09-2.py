#!/usr/bin/env python3

directions = {
    'U': (0, 1),
    'D': (0, -1),
    'R': (1, 0),
    'L': (-1, 0),
}


def solve(file_name):
    path = ''
    for line in open(file_name, 'r'):
        direction, length = line.split()
        path += direction * int(length)
    coord = [(0, 0)] * 10
    path_t = [(0, 0)]
    for m in path:
        coord[0] = (coord[0][0] + directions[m][0], coord[0][1] + directions[m][1])
        for i in range(1, 10):
            if dist(coord[i-1], coord[i]) > 1:
                coord[i] = (coord[i][0] + sign(coord[i-1][0] - coord[i][0]), coord[i][1] + sign(coord[i-1][1] - coord[i][1]))
                if i == 9:
                    path_t.append(coord[i])
    print(len(set(path_t)), path_t)
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
    assert solve('09-test.txt') == 1
    assert solve('09-test2.txt') == 36
    assert solve('09.txt') == 2485
