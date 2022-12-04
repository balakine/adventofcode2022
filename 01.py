#!/usr/bin/env python3
import sys


def solve(file_name):
    elves = []
    elf = 1
    calories = 0
    for line in open(file_name, 'r'):
        if line.strip():
            calories += int(line.strip())
        else:
            elves.append({'elf': elf, 'calories': calories})
            elf += 1
            calories = 0
    elves_by_calories = sorted(elves, key=lambda d: d['calories'], reverse=True)
    print(sum(x['calories'] for x in elves_by_calories[0:3]))


if __name__ == "__main__":
    solve(sys.argv[1])
