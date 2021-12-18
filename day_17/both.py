#!/usr/bin/env python3

import pprint as pp
from z3 import *

def parse(input):
    lines = [l.strip() for l in open(input)]
    splits = lines[0].split()
    x_s = splits[2][2:-1].split('.')
    x_min = int(x_s[0])
    x_max = int(x_s[-1])

    y_s = splits[3][2:].split('.')
    y_min = int(y_s[0])
    y_max = int(y_s[-1])

    return x_min, x_max, y_min, y_max


def shoot(x_vel, y_vel, grid, y_min, debug=False):
    x = 0
    y = 0
    max_y = 0

    while y >= y_min:
        x += x_vel
        y += y_vel

        if y > max_y:
            max_y = y

        if (x,y) in grid:
            if debug: print(f'Passed zone at {(x,y) = }, {max_y = }')
            return True, max_y

        if x_vel > 0:
            x_vel -= 1
        if x_vel < 0:
            x_vel += 1
        y_vel -= 1

    if debug: print(f'Failed to pass zone, {max_y = }')
    return False, max_y


def part1(input, debug=False):
    x_min, x_max, y_min, y_max = parse(input)
    if debug: print(x_min, x_max, y_min, y_max)

    grid = {}
    for x in range(x_min, x_max+1):
        for y in range(y_min, y_max+1):
            grid[(x,y)] = True

    max_y = 0
    for xv in range(100):
        for yv in range(100):
            passing, max_y_n = shoot(xv, yv, grid, y_min)
            if passing:
                if max_y_n > max_y:
                    max_y = max_y_n
                    if debug: print(f'{xv = } {yv = } {max_y = }')
    
    print(f'Part 1 {input}: {max_y = }')


def part2(input, debug=False):
    x_min, x_max, y_min, y_max = parse(input)
    if debug: print(x_min, x_max, y_min, y_max)

    grid = {}
    for x in range(x_min, x_max+1):
        for y in range(y_min, y_max+1):
            grid[(x,y)] = True

    uniq = set()
    for xv in range(0, 500):
        for yv in range(y_min, 500):
            passing, max_y_n = shoot(xv, yv, grid, y_min)
            if passing:
                uniq.add((xv,yv))
                if debug: print(f'{xv = } {yv = } {len(uniq) = }')
    
    print(f'Part 2 {input}: {len(uniq) = }')


def part2_z3(input, debug=False):
    x_min, x_max, y_min, y_max = parse(input)
    if debug: print(x_min, x_max, y_min, y_max)

    s = Optimize()

    xv = Int('xv')
    x = Int('x')
    x_drag = Int('x_drag')
    yv = Int('yv')
    y = Int('y')
    t = Int('t')

    s.add(t > 0)
    s.add(And(xv >= 0, xv < 500))
    s.add(And(yv > -500, yv < 500))
    s.add(x_drag == (t*(t+1))/2)
    s.add(x == If(t < xv, xv * t - x_drag, (xv*(xv+1))/2))
    s.add(y == yv * t - (t * (t + 1) / 2))

    s.add(And(x >= x_min, x <= x_max))
    s.add(And(y >= y_min, y <= y_max))

    print(s)
    
    grid = {}
    for xi in range(x_min, x_max+1):
        for yi in range(y_min, y_max+1):
            grid[(xi,yi)] = True

    passing_cnt = 0
    while True:
        ret = s.check()
        if ret == sat:
            m = s.model()
            passing, _ = shoot(m[xv].as_long(), m[yv].as_long(), grid, y_min, True)
            if passing: passing_cnt += 1
            print(m)
            print(f'{m[xv]} {m[yv]} -> ({m[x]}, {m[y]}) {passing = } {passing_cnt = }')
            print()
            s.add(Or(xv != m[xv], yv != m[yv]))
        else:
            print(ret)
            break


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')

# part2_z3('example.txt')