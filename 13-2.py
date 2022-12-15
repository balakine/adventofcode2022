#!/usr/bin/env python3

class Packet:
    x = []

    def __init__(self, x):
        self.x = x

    def __lt__(self, other):
        if right_order(self.x, other.x) == 1:
            return True
        return False

    def __eq__(self, other):
        if right_order(self.x, other.x) == 0:
            return True
        return False

    def __str__(self):
        return str(self.x)


divider1 = Packet([[2]])
divider2 = Packet([[6]])


def solve(file_name):
    lines = open(file_name, 'r').readlines()
    packets = [Packet(eval(line)) for line in lines if line != '\n']
    packets.append(divider1)
    packets.append(divider2)
    packets.sort()
    divider1_index = packets.index(divider1) + 1
    divider2_index = packets.index(divider2) + 1
    decoder_key = divider1_index * divider2_index
    print(f'{divider1_index} * {divider2_index} = {decoder_key}')
    return decoder_key


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


if __name__ == "__main__":
    assert solve('13-test.txt') == 140
    assert solve('13.txt') == 20758
