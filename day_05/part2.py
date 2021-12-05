#!/usr/bin/env python3

import sys
import pprint as pp

def dbg(msg = None):
    print(f"line {sys._getframe().f_back.f_lineno:4}: {msg if msg is not None else ''}")

lines = [line.strip() for line in open('input.txt')]

# print(lines)

grid = {}

def add_grid(coord):
    if coord in grid:
        grid[coord] += 1
    else:
        grid[coord] = 1

def print_grid():
    for y in range(10):
        for x in range(10):
            coord = (x, y)
            if coord in grid:
                print(grid[coord], end='')
            else:
                print('.', end='')
        print()

for line in lines:
    # print(line)
    splits = line.split(' ')
    x1, y1 = splits[0].split(',')
    x2, y2 = splits[2].split(',')
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)

    if x1 == x2:
        # print('horizontal')
        for y in range(y1, y2+1):
            add_grid((x1, y))
        for y in range(y2, y1+1):
            add_grid((x1, y))
    elif y1 == y2:
        # print('vertical')
        for x in range(x1, x2+1):
            add_grid((x, y1))
        for x in range(x2, x1+1):
            add_grid((x, y1))
    else:
        # print('diagonal')
        while x1 != x2 and y1 != y2:
            add_grid((x1, y1))
            if x1 < x2:
                x1 += 1
            else:
                x1 -= 1
            if y1 < y2:
                y1 += 1
            else:
                y1 -= 1
        add_grid((x1, y1))

#print_grid()

#pp.pprint(grid)

sum = 0
for k in grid.values():
    if k >= 2:
        sum += 1
print(sum)
