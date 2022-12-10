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
    print(len(byte_code))
    signal_strength = 0
    for i in range(20, 221, 40):
        signal_strength += byte_code[i-1] * i
    print(signal_strength)
    return signal_strength


if __name__ == "__main__":
    assert solve('10-test.txt') == 13140
    assert solve('10.txt') == 17940
