#!/usr/bin/env python3

directions = [
    (0, 1),   # down
    (-1, 1),  # down left
    (1, 1),   # down right
]


def solve(file_name):
    max_x = 1000
    max_y = 200
    cave = [[0] * max_y for _ in range(max_x)]
    for line in open(file_name, 'r'):
        coords = line.strip().split(' ->')
        for i in range(len(coords) - 1):
            x, y = map(int, coords[i].split(','))
            length, dx, dy = direction(x, y, *map(int, coords[i + 1].split(',')))
            for j in range(length + 1):
                cave[x + dx * j][y + dy * j] = 1

    units_of_sand = 0
    while True:
        x, y = (500, 0)
        falling = True
        while falling:
            for dx, dy in directions:
                if y + dy == max_y:  # into the endless void
                    for ty in range(10):
                        for tx in range(493, 504):
                            print(cave[tx][ty], end='')
                        print()
                    print(units_of_sand)
                    return units_of_sand
                if cave[x + dx][y + dy] == 0:
                    x += dx
                    y += dy
                    break  # keep falling
            else:
                cave[x][y] = 2  # come to rest
                falling = False
                units_of_sand += 1


def direction(ax, ay, bx, by):
    return [max(abs(bx - ax), abs(by - ay)), sign(bx - ax), sign(by - ay)]


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0


if __name__ == "__main__":
    assert solve('14-test.txt') == 24
    assert solve('14.txt') == 888
