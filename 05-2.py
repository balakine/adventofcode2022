#!/usr/bin/env python3


def solve(file_name):
    file = open(file_name, 'r')
    stacks = []
    while (line := file.readline()) != '\n':
        crates = [line[i:i+4] for i in range(0, len(line), 4)]
        while len(stacks) < len(crates):
            stacks.append([])
        for i, crate in enumerate(crates):
            if (k := crate[1:2]) != ' ':
                stacks[i].append(k)
    # The last crate is actually the stack label
    labeled_stacks = {s.pop(): list(reversed(s)) for s in stacks}
    print(labeled_stacks)
    while line := file.readline():
        _, count, _, source, _, dest = line.split()
        labeled_stacks[dest] += labeled_stacks[source][-int(count):]
        del labeled_stacks[source][-int(count):]
        print(labeled_stacks)

    top = ''.join([labeled_stacks[s].pop() for s in sorted(labeled_stacks.keys())])
    print(top)
    return top


if __name__ == "__main__":
    assert solve('05-test.txt') == 'MCD'
    assert solve('05.txt') == 'GGNPJBTTR'
