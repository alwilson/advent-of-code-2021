#!/usr/bin/env python3

import pprint as pp
from z3 import *

def parse(input):
    lines = [l.strip() for l in open(input)]
    return lines


def process(line_l: list):
    depth = 0
    explode = False
    next_l = line_l
    new_line = ''
    prev = []
    while True:
        print(next_l, depth, prev)
        if depth == 4:
            print('explode', next_l)
            explode = True
            exit(0)
        
        cont = False
        for l in next_l:
            if type(l) is list:
                prev.append(next_l)
                next_l = l
                new_line += '['
                depth += 1
                cont = True
                break
            if type(l) is int:
                new_line += str(l)
        
        if cont:
            continue

        if len(prev) == 0:
            break

        next_l = prev.pop()
        new_line += ']'
        depth -= 1

    return line


def part1(input, debug=False):
    lines = parse(input)

    for line in lines:
        if debug: print(line) 
        a = compile(line, '', 'eval')
        line_l = eval(a)
        print(line_l)
        process(line_l)
    # print(f'Part 1 {input}: {max_y = }')


# def part2(input, debug=False):
#     x_min, x_max, y_min, y_max = parse(input)
#     if debug: print(x_min, x_max, y_min, y_max)
# 
#     grid = {}
#     for x in range(x_min, x_max+1):
#         for y in range(y_min, y_max+1):
#             grid[(x,y)] = True
# 
#     uniq = set()
#     for xv in range(0, 500):
#         for yv in range(y_min, 500):
#             passing, max_y_n = shoot(xv, yv, grid, y_min)
#             if passing:
#                 uniq.add((xv,yv))
#                 if debug: print(f'{xv = } {yv = } {len(uniq) = }')
#     
#     print(f'Part 2 {input}: {len(uniq) = }')


part1('example.txt', True)
# part1('input.txt')
# 
# part2('example.txt')
# part2('input.txt')