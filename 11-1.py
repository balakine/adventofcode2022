#!/usr/bin/env python3

def solve(file_name):
    monkeys = {}
    for line in open(file_name, 'r'):
        if line == '\n':
            continue
        key, value = line.strip().split(':')
        value = value.strip()
        if key.startswith('Monkey'):
            monkey_label = key.split()[1]
        elif key == 'Starting items':
            items = list(map(int, value.split(', ')))
        elif key == 'Operation':
            op = value.split('=')[1]
        elif key == 'Test':
            test = int(value.split()[2])
        elif key == 'If true':
            m_true = value.split()[3]
        elif key == 'If false':
            m_false = value.split()[3]
            monkeys[monkey_label] = {
                'items': items,
                'op': op,
                'test': test,
                'm_true': m_true,
                'm_false': m_false,
                'inspected': 0,
            }
    for i in range(20):
        for k in monkeys.keys():
            monkey = monkeys[k]
            monkey['inspected'] += len(monkey['items'])
            while monkey['items']:
                j = monkey['items'].pop()
                new = eval(monkey['op'].replace('old', str(j))) // 3
                if new % monkey['test'] == 0:
                    monkeys[monkey['m_true']]['items'].append(new)
                else:
                    monkeys[monkey['m_false']]['items'].append(new)
    m = [v['inspected'] for k, v in monkeys.items()]
    m.sort(reverse=True)
    print(m)
    # print(monkeys)
    monkey_business = m[0] * m[1]
    print(monkey_business)
    return monkey_business


if __name__ == "__main__":
    assert solve('11-test.txt') == 10605
    assert solve('11.txt') == 55944
