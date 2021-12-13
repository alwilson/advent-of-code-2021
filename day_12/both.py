#!/usr/bin/env python3

import pprint as pp

def parse(input, caves):
    lines = [l.strip() for l in open(input)]
    for l in lines:
        l_split = l.split('-')
        left = l_split[0]
        right = l_split[1]

        if left not in caves:
            caves[left] = [right]
        else:
            caves[left].append(right)

        if right not in caves:
            caves[right] = [left]
        else:
            caves[right].append(left)

def explore(caves, node, visited, routes):
    if node == 'end':
        visited.append(node)
        routes.append(visited)

    for n in caves[node]:
        if n.islower() and n not in visited or n.isupper():
            explore(caves, n, visited + [node], routes)

def explore_twice(caves, node, visited, routes, small_visited_twice):
    if node == 'end':
        visited.append(node)
        routes.append(visited)

    for n in caves[node]:
        if n.islower() and visited.count(n) < (2 - small_visited_twice) and n != 'start':
            if visited.count(n) == 1:
                explore_twice(caves, n, visited + [node], routes, 1)
            else:
                explore_twice(caves, n, visited + [node], routes, small_visited_twice)
        
        if n.isupper():
            explore_twice(caves, n, visited + [node], routes, small_visited_twice)

def part1(input, debug=False):
    caves = {}
    parse(input, caves)
    if debug: pp.pprint(caves)

    routes = []
    explore(caves, 'start', [], routes)
    if debug: pp.pprint(routes)
    print(f'Part 1 {input}: {len(routes)}')


def part2(input, debug=False):
    caves = {}
    parse(input, caves)
    if debug: pp.pprint(caves)

    routes = []
    explore_twice(caves, 'start', [], routes, 0)
    if debug: pp.pprint(routes)
    print(f'Part 2 {input}: {len(routes)}')

part1('lil_example.txt')
part1('example.txt')
part1('larger_example.txt')
part1('input.txt')

part2('lil_example.txt')
part2('example.txt')
part2('larger_example.txt')
part2('input.txt')