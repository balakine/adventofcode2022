#!/usr/bin/env python3
import sys
from itertools import zip_longest


def solve(file_name):
    total_priority = 0
    f = open(file_name, 'r')
    for line1, line2, line3 in grouper(f, 3):
        items1 = set(line1.strip())
        items2 = set(line2.strip())
        items3 = set(line3.strip())
        badge = items1.intersection(items2.intersection(items3))
        total_priority += priority(badge.pop())
    print(total_priority)


def grouper(iterable, n, *, incomplete='fill', fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, fillvalue='x') --> ABC DEF Gxx
    # grouper('ABCDEFG', 3, incomplete='strict') --> ABC DEF ValueError
    # grouper('ABCDEFG', 3, incomplete='ignore') --> ABC DEF
    args = [iter(iterable)] * n
    if incomplete == 'fill':
        return zip_longest(*args, fillvalue=fillvalue)
    if incomplete == 'strict':
        return zip(*args, strict=True)
    if incomplete == 'ignore':
        return zip(*args)
    else:
        raise ValueError('Expected fill, strict, or ignore')


def priority(x):
    i = ord(x)
    if i in range(ord('a'), ord('z') + 1):
        return 1 + i - ord('a')
    if i in range(ord('A'), ord('Z') + 1):
        return 27 + i - ord('A')


if __name__ == "__main__":
    solve(sys.argv[1])
