#!/usr/bin/env python3

with open('input.txt') as fd:
    commands = [line.strip().split() for line in fd]

h = 0
d = 0
for c in commands:
    direct = c[0]
    val = int(c[1])

    if direct == 'forward':
        h += val
    if direct == 'down':
        d += val
    if direct == 'up':
        d -= val

print(h*d)