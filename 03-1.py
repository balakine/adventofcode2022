#!/usr/bin/env python3
import sys


def solve(file_name):
    total_priority = 0
    for line in open(file_name, 'r'):
        items = line.strip()
        compartment_length = len(items) // 2
        first_compartment = set(items[:compartment_length])
        second_compartment = set(items[compartment_length:])
        need_repacking = first_compartment.intersection(second_compartment)
        total_priority += sum(priority(x) for x in need_repacking)
    print(total_priority)


def priority(x):
    i = ord(x)
    if i in range(ord('a'), ord('z') + 1):
        return 1 + i - ord('a')
    if i in range(ord('A'), ord('Z') + 1):
        return 27 + i - ord('A')


if __name__ == "__main__":
    solve(sys.argv[1])
