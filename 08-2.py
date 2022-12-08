#!/usr/bin/env python3

def solve(file_name):
    t = []
    n = []
    e = []
    s = []
    w = []
    for line in open(file_name, 'r'):
        t.append(list(map(int, list(line.strip()))))
        n.append([0] * len(t[-1]))
        e.append([0] * len(t[-1]))
        s.append([0] * len(t[-1]))
        w.append([0] * len(t[-1]))
    for i in range(len(t)):
        for j in range(len(t[i])):
            d = 0
            for k in range(j-1, -1, -1):
                d += 1
                if t[i][j] <= t[i][k]:
                    break
            w[i][j] = d
    for i in range(len(t)):
        for j in reversed(range(len(t[i]))):
            d = 0
            for k in range(j+1, len(t[i])):
                d += 1
                if t[i][j] <= t[i][k]:
                    break
            e[i][j] = d
    for j in range(len(t[0])):
        for i in range(len(t)):
            d = 0
            for k in range(i-1, -1, -1):
                d += 1
                if t[i][j] <= t[k][j]:
                    break
            n[i][j] = d
    for j in range(len(t[0])):
        for i in reversed(range(len(t))):
            d = 0
            for k in range(i+1, len(t)):
                d += 1
                if t[i][j] <= t[k][j]:
                    break
            s[i][j] = d
    scenic_score = 0
    for i in range(len(t)):
        for j in range(len(t[i])):
            if w[i][j] * e[i][j] * n[i][j] * s[i][j] > scenic_score:
                scenic_score = w[i][j] * e[i][j] * n[i][j] * s[i][j]
    print(scenic_score)
    return scenic_score


if __name__ == "__main__":
    assert solve('08-test.txt') == 8
    assert solve('08.txt') == 383520
