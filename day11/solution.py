# DISCLAIMER: Lines with no text are removed from the input file.

import math

class Monkey:
    def __init__(self, n, i, o, t, mt, mf, c):
        self.name = n
        self.items = i
        self.op = o
        self.test = t
        self.m_true = mt
        self.m_false = mf
        self.count = c

    def inspect(self, m):
        # End turn if there are no items
        if len(self.items) < 0:
            return
        for _ in range(len(self.items)):
            buffer = self.items[0]
            self.items.pop(0)
            self.count += 1
            buffer = math.floor(eval(self.op, {'old': buffer}) / 3)
            if buffer % self.test == 0:
                m[self.m_true].items.append(buffer)
            else:
                m[self.m_false].items.append(buffer)

def start_rounds(n, monkeys, m):
    for _ in range(n):
        for i in range(len(monkeys)):
            m[i].inspect(m)

# Create monkeys
monkeys = []
with open("input.txt", "r") as f:
    while True:
        try:
            lines = [next(f) for _ in range(6)]
            name = int(lines[0].strip().split()[1].rstrip(':'))
            items = list(map(int, lines[1].strip()[16:].split(', ')))
            op = lines[2].strip()[16:]
            test = int(lines[3].strip().split()[3])
            m_true = int(lines[4].strip().split()[5])
            m_false = int(lines[5].strip().split()[5])
            c = 0
            # Create and add monkey to list
            monkeys.append(Monkey(name, items, op, test, m_true, m_false, c))
        except StopIteration:
            break

# Create dict for monkeys. Usage: m[name]
m = {}
for monkey in monkeys:
    m[monkey.name] = monkey

start_rounds(20, monkeys, m)

mb = []
for i in range(len(monkeys)):
    mb.append(m[i].count)
mb = sorted(mb, reverse=True)
print(f"Monkey Business: {mb[0]*mb[1]}")