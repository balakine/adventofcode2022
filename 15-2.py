#!/usr/bin/env python3
import re


def solve_range(file_name, search_space):
    sensors = []
    for line in open(file_name, 'r'):
        sx, sy, bx, by = map(int, re.findall(r'-?\d+', line))
        sensors.append([sx, sy, distance((sx, sy), (bx, by))])
    for y in range(search_space + 1):
        c = solve(sensors, y, search_space)
        if c > -1:
            tuning_frequency = c * 4_000_000 + y
            print(c, y, tuning_frequency)
            return tuning_frequency


def solve(sensors, row, search_space):
    row_coverage = []
    for sx, sy, d in sensors:
        if abs(sy - row) > d:
            continue  # this sensor doesn't cover the row
        row_from = max(sx - (d - abs(sy - row)), 0)
        row_to = min(sx + (d - abs(sy - row)), search_space)
        new_row_coverage = list(row_coverage)
        for segment in row_coverage:
            i_row_from, i_row_to = segment
            if overlap((row_from, row_to), (i_row_from, i_row_to)):
                # merge into a new segment
                row_from = min(row_from, i_row_from)
                row_to = max(row_to, i_row_to)
                new_row_coverage.remove(segment)
        new_row_coverage.append([row_from, row_to])
        row_coverage = new_row_coverage
    s = sum([x[1] - x[0] + 1 for x in row_coverage])
    if s == search_space + 1:
        return -1
    if len(row_coverage) == 1:
        if row_coverage[0][0] > 0:
            return 0
        if row_coverage[0][1] < search_space:
            return search_space
    elif len(row_coverage) == 2:
        return min(row_coverage[0][1], row_coverage[1][1]) + 1
    return -1


def overlap(a, b):
    # overlap or adjacent
    return (
            a[0] <= b[0] - 1 <= a[1] or
            a[0] <= b[1] + 1 <= a[1] or
            b[0] <= a[0] - 1 <= b[1] or
            b[0] <= a[1] + 1 <= b[1])


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


if __name__ == "__main__":
    assert solve_range('15-test.txt', 20) == 56_000_011
    assert solve_range('15.txt', 4_000_000) == 12_977_110_973_564
