#!/usr/bin/env python3
import sys

POINTS_FOR_HAND = {'X': 1, 'Y': 2, 'Z': 3}
POINTS_FOR_OUTCOME = {
    'A': {'X': 3, 'Y': 6, 'Z': 0},
    'B': {'X': 0, 'Y': 3, 'Z': 6},
    'C': {'X': 6, 'Y': 0, 'Z': 3}
}


def solve(file_name):
    points = 0
    for line in open(file_name, 'r'):
        his, mine = line.split()
        points += POINTS_FOR_HAND[mine] + POINTS_FOR_OUTCOME[his][mine]
    print(points)


if __name__ == "__main__":
    solve(sys.argv[1])
