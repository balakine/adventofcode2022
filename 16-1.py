#!/usr/bin/env python3
import re


def solve(file_name, row):
    sensors = []
    beacons_in_row = set()
    for line in open(file_name, 'r'):
        sx, sy, bx, by = map(int, re.findall(r'-?\d+', line))
        sensors.append([sx, sy, distance((sx, sy), (bx, by))])
        if by == row:
            beacons_in_row.add((bx, by))

    row_coverage = []
    for sx, sy, d in sensors:
        if abs(sy - row) > d:
            continue  # this sensor doesn't cover the row
        row_from = sx - (d - abs(sy - row))
        row_to = sx + (d - abs(sy - row))
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
        print(row_coverage)
    s = sum([x[1] - x[0] + 1 for x in row_coverage]) - len(beacons_in_row)
    print(s, len(beacons_in_row))
    return s


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
    assert solve('15-test.txt', 10) == 26
    assert solve('15.txt', 2_000_000) == 4827924
