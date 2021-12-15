#!/usr/bin/env python3

import pprint as pp

def parse(input):
    lines = [l.strip() for l in open(input)]

    risk = {}
    for y, line in enumerate(lines):
        for x, num in enumerate(line):
            risk[(x, y)] = int(num)

    return risk

def print_risk(risk):
    x_min = min([num[0] for num in risk.keys()])
    x_max = max([num[0] for num in risk.keys()])
    y_min = min([num[1] for num in risk.keys()])
    y_max = max([num[1] for num in risk.keys()])

    for y in range(y_min, y_max+1):
        for x in range(x_min, x_max+1):
            print(risk[(x,y)], end='')
        print()

def walk(risk, start, stop):
    frontier = {}
    frontier[start] = 0
    visited = {}
    total = len(risk.keys())

    while True:
        lowest = min(frontier, key=frontier.get)
        value = frontier[lowest]
        del(frontier[lowest])
        visited[lowest] = True

        x = lowest[0]
        y = lowest[1]
        for next_pos in [(x+1,y), (x,y+1), (x-1,y), (x,y-1)]:
            if next_pos not in visited and next_pos in risk:
                if next_pos in frontier:
                    frontier[next_pos] = min(frontier[next_pos], value + risk[next_pos])
                else:
                    frontier[next_pos] = value + risk[next_pos]
                if next_pos == stop:
                    return frontier[next_pos]

def part1(input, debug=False):
    risk = {}

    risk = parse(input)
    x_min = min([num[0] for num in risk.keys()])
    x_max = max([num[0] for num in risk.keys()])
    y_min = min([num[1] for num in risk.keys()])
    y_max = max([num[1] for num in risk.keys()])

    # print_risk(risk)

    cost = walk(risk, (x_min, y_min), (x_max, y_max))
    print(f'Part 1 {input}: {cost}')

def part2(input, debug=False):
    risk = {}

    risk = parse(input)
    x_min = min([num[0] for num in risk.keys()])
    x_max = max([num[0] for num in risk.keys()])
    y_min = min([num[1] for num in risk.keys()])
    y_max = max([num[1] for num in risk.keys()])

    keys = list(risk.keys())
    for key in keys:
        for n in range(1,5):
            new_val = risk[key] + n
            risk[(key[0]+(x_max+1)*n, key[1])] = new_val - 9 if new_val > 9 else new_val
    
    keys = list(risk.keys())
    for key in keys:
        for n in range(1,5):
            new_val = risk[key] + n
            risk[(key[0], key[1]+(y_max+1)*n)] = new_val - 9 if new_val > 9 else new_val

    # print_risk(risk)

    x_min = min([num[0] for num in risk.keys()])
    x_max = max([num[0] for num in risk.keys()])
    y_min = min([num[1] for num in risk.keys()])
    y_max = max([num[1] for num in risk.keys()])
    cost = walk(risk, (x_min, y_min), (x_max, y_max))
    print(f'Part 2 {input}: {cost}')

part1('example.txt')
part1('input.txt')
 
part2('example.txt')
part2('input.txt')