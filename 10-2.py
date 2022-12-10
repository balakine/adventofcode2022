#!/usr/bin/env python3

def solve(file_name):
    byte_code = []
    x = 1
    for line in open(file_name, 'r'):
        command = line.split()
        if command[0] == 'noop':
            byte_code.append(x)
        elif command[0] == 'addx':
            byte_code.append(x)
            byte_code.append(x)
            x += int(command[1])
    signal = ''
    for cycle in range(0, 240):
        if abs(byte_code[cycle] - cycle % 40) <= 1:
            signal += '#'
        else:
            signal += '.'
    for row in range(6):
        print(signal[row*40:row*40+40])
    return signal


if __name__ == "__main__":
    assert solve('10-test.txt') == \
        '##..##..##..##..##..##..##..##..##..##..' + \
        '###...###...###...###...###...###...###.' + \
        '####....####....####....####....####....' + \
        '#####.....#####.....#####.....#####.....' + \
        '######......######......######......####' + \
        '#######.......#######.......#######.....'
    print()
    assert solve('10.txt') == \
'####..##..###...##....##.####...##.####.' \
'...#.#..#.#..#.#..#....#.#.......#....#.' \
'..#..#....###..#..#....#.###.....#...#..' \
'.#...#....#..#.####....#.#.......#..#...' \
'#....#..#.#..#.#..#.#..#.#....#..#.#....' \
'####..##..###..#..#..##..#.....##..####.'
