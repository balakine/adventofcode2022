#!/usr/bin/env python3
import sys


def solve(file_name):
    overlaps = 0
    for line in open(file_name, 'r'):
        range0, range1 = line.split(',')
        ranges = [{}, {}]
        ranges[0]['start'], ranges[0]['end'] = map(int, range0.split('-'))
        ranges[1]['start'], ranges[1]['end'] = map(int, range1.split('-'))
        # Shorter range first
        ranges.sort(key=lambda d: d['end'] - d['start'])
        if ranges[0]['start'] >= ranges[1]['start'] and ranges[0]['end'] <= ranges[1]['end']:
            overlaps += 1
    print(overlaps)


if __name__ == "__main__":
    solve(sys.argv[1])
