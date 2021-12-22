#!/usr/bin/env python3

import functools

def parse(input):
    lines = [l.strip() for l in open(input)]
    p1 = int(lines[0].split()[-1])
    p2 = int(lines[1].split()[-1])

    return p1, p2


def turn(p, score, roll, roll_total, debug=False):
    for _ in range(3):
        p += roll
        roll += 1
        roll_total += 1
        if roll > 100: roll %= 100
        p %= 10
        if p == 0: p = 10
    score += p
    if debug: print(f'({roll_total}) {p = } {score = }')

    return p, score, roll, roll_total


def part1(input, debug=False):
    p1, p2 = parse(input)
    p1_score = 0
    p2_score = 0
    if debug: print(f'Part 1 {input}: {p1 = } {p2 = } {p1_score = } {p2_score = }')

    roll = 1
    roll_total = 0
    while True:
        p1, p1_score, roll, roll_total = turn(p1, p1_score, roll, roll_total)
        if p1_score >= 1000:
            break
        
        p2, p2_score, roll, roll_total = turn(p2, p2_score, roll, roll_total)
        if p2_score >= 1000:
            break
    
    if debug: print(f'{roll = } {p1 = } {p2 = } {p1_score = } {p2_score = }')
    print(f'Part 1 {input}: {roll_total*min(p1_score,p2_score) = }')


def qturn(p, roll):
    for _ in range(3):
        p += roll
        p %= 10
        if p == 0: p = 10
    return p


@functools.cache
def round(p1, p2, p1_score, p2_score, step):
    if p1 > 10: p1 %= 10
    if p2 > 10: p2 %= 10

    if step == 3: p1_score += p1
    if step == 6: p2_score += p2
    
    if p1_score >= 21: return 1
    if p2_score >= 21: return 1j

    step %= 6

    wins = 0
    if step < 3:
        for i in [1,2,3]:
            wins += round(p1+i, p2, p1_score, p2_score, step+1)
    else: 
        for i in [1,2,3]:
            wins += round(p1, p2+i, p1_score, p2_score, step+1)

    return wins


def part2(input, debug=False):
    p1, p2 = parse(input)
    wins = round(p1, p2, 0, 0, 0)
    print(f'Part 2 {input}: {int(max(wins.real, wins.imag)) = }')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')