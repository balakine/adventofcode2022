#!/usr/bin/env python3
import sys

POINTS_FOR_OUTCOME = {'X': 0, 'Y': 3, 'Z': 6}
POINTS_FOR_HAND = {'A': 1, 'B': 2, 'C': 3}
RULES = {
    'A': {'X': 'C', 'Y': 'A', 'Z': 'B'},
    'B': {'X': 'A', 'Y': 'B', 'Z': 'C'},
    'C': {'X': 'B', 'Y': 'C', 'Z': 'A'}
}


def solve(file_name):
    points = 0
    for line in open(file_name, 'r'):
        his, outcome = line.split()
        mine = RULES[his][outcome]
        points += POINTS_FOR_HAND[mine] + POINTS_FOR_OUTCOME[outcome]
    print(points)


if __name__ == "__main__":
    solve(sys.argv[1])
