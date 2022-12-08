#!/usr/bin/env python3

def solve(file_name):
    t = []
    n = []
    e = []
    s = []
    w = []
    for line in open(file_name, 'r'):
        t.append(list(map(int, list(line.strip()))))
        n.append([1] * len(t[-1]))
        e.append([1] * len(t[-1]))
        s.append([1] * len(t[-1]))
        w.append([1] * len(t[-1]))
    for i in range(len(t)):
        current_highest = -1
        for j in range(len(t[i])):
            if t[i][j] > current_highest:
                current_highest = t[i][j]
            else:
                w[i][j] = 0
    for i in range(len(t)):
        current_highest = -1
        for j in reversed(range(len(t[i]))):
            if t[i][j] > current_highest:
                current_highest = t[i][j]
            else:
                e[i][j] = 0
    for j in range(len(t[0])):
        current_highest = -1
        for i in range(len(t)):
            if t[i][j] > current_highest:
                current_highest = t[i][j]
            else:
                n[i][j] = 0
    for j in range(len(t[0])):
        current_highest = -1
        for i in reversed(range(len(t))):
            if t[i][j] > current_highest:
                current_highest = t[i][j]
            else:
                s[i][j] = 0
    visible = 0
    for i in range(len(t)):
        for j in range(len(t[i])):
            if w[i][j] or e[i][j] or n[i][j] or s[i][j]:
                visible += 1
    print(visible)
    return visible


if __name__ == "__main__":
    assert solve('08-test.txt') == 21
    assert solve('08.txt') == 1816
