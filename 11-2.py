#!/usr/bin/env python3

def solve(file_name):
    monkeys = []
    items = []
    for line in open(file_name, 'r'):
        if line == '\n':
            continue
        key, value = line.strip().split(':')
        value = value.strip()
        if key.startswith('Monkey'):
            monkey_label = int(key.split()[1])
        elif key == 'Starting items':
            m_i = list(map(int, value.split(', ')))
            for item in m_i:
                items.append({
                    'worry': item,
                    'monkey_label': monkey_label
                })
        elif key == 'Operation':
            op = compile(value.split('=')[1].strip(), '<string>', 'eval')
        elif key == 'Test':
            test = int(value.split()[2])
        elif key == 'If true':
            m_true = int(value.split()[3])
        elif key == 'If false':
            m_false = int(value.split()[3])
            # assume monkeys are in order
            monkeys.append({
                'op': op,
                'test': test,
                'm_true': m_true,
                'm_false': m_false,
                'inspected': 0,
            })
    for item in items:
        r = []
        for monkey in monkeys:
            r.append(item['worry'] % monkey['test'])
        item['r'] = r
    for _ in range(10000):
        for monkey_label, monkey in enumerate(monkeys):
            monkey_items = filter(lambda j: j['monkey_label'] == monkey_label, items)
            for item in monkey_items:
                monkey['inspected'] += 1
                for i, r in enumerate(item['r']):
                    old = r
                    # eval uses `old`
                    new = eval(monkey['op'])
                    item['r'][i] = new % monkeys[i]['test']
                if item['r'][monkey_label] == 0:
                    item['monkey_label'] = monkey['m_true']
                else:
                    item['monkey_label'] = monkey['m_false']
    m = [v['inspected'] for v in monkeys]
    m.sort(reverse=True)
    print(m)
    print(items)
    monkey_business = m[0] * m[1]
    print(monkey_business)
    return monkey_business


if __name__ == "__main__":
    assert solve('11-test.txt') == 2713310158
    assert solve('11.txt') == 15117269860
