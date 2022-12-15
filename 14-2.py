#!/usr/bin/env python3

directions = [
    (0, 1),   # down
    (-1, 1),  # down left
    (1, 1),   # down right
]


def solve(file_name):
    max_x = 1000
    max_y = 200
    max_y_f = 0
    cave = [[0] * max_y for _ in range(max_x)]
    for line in open(file_name, 'r'):
        coords = line.strip().split(' ->')
        for i in range(len(coords) - 1):
            x, y = map(int, coords[i].split(','))
            length, dx, dy = direction(x, y, *map(int, coords[i + 1].split(',')))
            for j in range(length + 1):
                cave[x + dx * j][y + dy * j] = 1
                max_y_f = (y + dy * j) if (y + dy * j) > max_y_f else max_y_f
    for i in range(max_x):
        cave[i][max_y_f + 2] = 1

    units_of_sand = 0
    while True:
        x, y = (500, 0)
        falling = True
        while falling:
            for dx, dy in directions:
                if y + dy == max_y:  # into the endless void
                    for ty in range(12):
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
                units_of_sand += 1
                cave[x][y] = 2  # come to rest
                if x == 500 and y == 0:
                    for ty in range(12):
                        for tx in range(493, 504):
                            print(cave[tx][ty], end='')
                        print()
                    print(units_of_sand)
                    return units_of_sand  # tthe source is blocked entirely
                falling = False


def direction(ax, ay, bx, by):
    return [max(abs(bx - ax), abs(by - ay)), sign(bx - ax), sign(by - ay)]


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0


if __name__ == "__main__":
    assert solve('14-test.txt') == 93
    assert solve('14.txt') == 26461
