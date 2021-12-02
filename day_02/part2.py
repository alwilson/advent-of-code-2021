#!/usr/bin/env python3

with open('input.txt') as fd:
    commands = [line.strip().split() for line in fd]

h = 0
d = 0
a = 0
for c in commands:
    direct = c[0]
    val = int(c[1])

    if direct == 'forward':
        h += val
        d += a * val
    if direct == 'down':
        a += val
    if direct == 'up':
        a -= val

print(h*d)