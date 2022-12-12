#!/usr/bin/env python3

directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]


def solve(file_name):
    heightmap = []
    visited_map = []
    path = []
    s = (0, 0)
    e = (0, 0)
    for line in open(file_name, 'r'):
        if 'S' in line:
            s = (len(heightmap), line.find('S'))
            line = line.replace('S', 'a')
        if 'E' in line:
            e = (len(heightmap), line.find('E'))
            line = line.replace('E', 'z')
        heightmap.append(list(line.strip()))
        visited_map.append([None] * len(line.strip()))
    path.append(e)
    visited_map[e[0]][e[1]] = 0
    while path:
        x, y = path.pop()
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            # check we are within the map
            if nx not in range(len(heightmap)) or ny not in range(len(heightmap[0])):
                continue
            # check if already visited
            if visited_map[nx][ny] is not None:
                continue
            # check the elevation difference is not too much
            if ord(heightmap[x][y]) - ord(heightmap[nx][ny]) > 1:
                continue
            # check if reached the target
            if heightmap[nx][ny] == 'a':
                print(f'Reached the target in {visited_map[x][y] + 1} steps')
                visualize(heightmap, visited_map, s, e)
                return visited_map[x][y] + 1
            visited_map[nx][ny] = visited_map[x][y] + 1
            path.insert(0, (nx, ny))
    visualize(heightmap, visited_map, s, e)
    return 0


def visualize(heightmap, visited_map, s, e):
    min_length = max(max(y for y in x if y is not None) for x in visited_map)
    for x, line in enumerate(heightmap):
        for y, c in enumerate(line):
            if s == (x, y) or e == (x, y):
                print(color2('X', visited_map[x][y], min_length), end='')
            else:
                print(color2(c, visited_map[x][y], min_length), end='')
        print()


def color2(s, ns, m):
    if s == 'X':
        return '\033[48:2:255:255:255m' + s + '\033[0m'
    bg = (ord(s) - ord('a')) * 192 // 26 + 63
    fg = (ns or 0) * 192 // m + 63
    return f'\033[48:2:0:{bg}:0m' + f'\033[38:2:{fg}:0:0m' + s + '\033[0m'


if __name__ == "__main__":
    assert solve('12-test.txt') == 29
    assert solve('12.txt') == 439
