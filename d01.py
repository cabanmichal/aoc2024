#!/usr/bin/env python3

from collections import Counter

F = "d01.txt"

a = []
b = []

with open(F) as fh:
    for line in fh:
        line = line.strip()
        if not line:
            continue
        l, r = line.split()
        a.append(int(l))
        b.append(int(r))

total = 0
for (x, y) in zip(sorted(a), sorted(b)):
    total += abs(x - y)

similarity = 0
counter = Counter(b)
for n in set(a):
    similarity += n * counter.get(n, 0)

print(total)  # 1651298
print(similarity)  # 21306195
