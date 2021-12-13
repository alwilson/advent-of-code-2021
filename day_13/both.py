#!/usr/bin/env python3

def parse(input, paper, instr):
    lines = [l.strip() for l in open(input)]
    for l in lines:
        if ',' in l:
            l_split = l.split(',')
            x = int(l_split[0])
            y = int(l_split[1])
            paper[(x,y)] = True
        if 'fold' in l:
            l_split = l.split()[2].split('=')
            instr.append((l_split[0], int(l_split[1])))


def print_paper(paper):
    x_min = min([dot[0] for dot in paper.keys()])
    x_max = max([dot[0] for dot in paper.keys()])
    y_min = min([dot[1] for dot in paper.keys()])
    y_max = max([dot[1] for dot in paper.keys()])

    for y in range(y_min, y_max+1):
        for x in range(x_min, x_max+1):
            if (x,y) in paper:
                print('█', end='')
            else:
                print(' ', end='')
        print()

def fold(i, paper):
    axis = i[0]
    dist = i[1]
    cur_dots = list(paper.keys())
    for dot in cur_dots:
        if axis == 'y':
            if dot[1] > dist:
                del(paper[dot])
                paper[(dot[0], 2*dist - dot[1])] = True
        else:
            if dot[0] > dist:
                del(paper[dot])
                paper[(2*dist - dot[0], dot[1])] = True

def part1(input, debug=False):
    paper = {}
    instr = []

    parse(input, paper, instr)

    for i in instr[:1]:
        fold(i, paper)

    print(f'Part 1 {input}: {len(paper.keys())}')
    if debug: print_paper(paper)


def part2(input, debug=False):
    paper = {}
    instr = []

    parse(input, paper, instr)

    for i in instr:
        fold(i, paper)

    print(f'Part 2 {input}: {len(paper)}')
    print_paper(paper)

part1('example.txt', True)
part1('input.txt')

part2('example.txt')
part2('input.txt')