#!/usr/bin/env python3
import re
from queue import Queue


def solve(file_name):
    cave = []
    for line in open(file_name, 'r'):
        weight = int(re.findall(r'\d+', line)[0])
        label, *links = re.findall(r'[A-Z]{2}', line)
        cave.append((label, weight, links))
    graph = []
    variants = Queue()
    location = 'AA'
    turn = 0
    for valve in cave:

    return 0


if __name__ == "__main__":
    assert solve('16-test.txt') == 0
    assert solve('16.txt') == 0
