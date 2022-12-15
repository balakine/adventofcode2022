#!/usr/bin/env python3
from itertools import zip_longest


def solve(file_name):
    file = open(file_name, 'r')
    pair_index = 1
    pairs_in_right_order = []
    for line1, line2, _ in grouper(file, 3):
        item1 = eval(line1)
        item2 = eval(line2)
        if right_order(item1, item2) == 1:
            pairs_in_right_order.append(pair_index)
        pair_index += 1
    s = sum(pairs_in_right_order)
    print(s, pairs_in_right_order)
    return s


def right_order(item1, item2):
    if type(item1) == int and type(item2) == int:
        if item1 < item2:
            return 1
        elif item1 > item2:
            return -1
        elif item1 == item2:
            return 0
    elif type(item1) == list and type(item2) == list:
        for i in range(min(len(item1), len(item2))):
            r = right_order(item1[i], item2[i])
            if r != 0:
                return r
        else:
            return right_order(len(item1), len(item2))
    elif type(item1) == int:
        return right_order([item1], item2)
    elif type(item2) == int:
        return right_order(item1, [item2])


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


if __name__ == "__main__":
    assert solve('13-test.txt') == 13
    assert solve('13.txt') == 6070
