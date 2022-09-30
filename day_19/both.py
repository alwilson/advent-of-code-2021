#!/usr/bin/env python3

import pprint as pp

def parse(input):
    lines = [l.strip() for l in open(input)]
    scanners = []
    beacons = []
    for line in lines:
        if '---' in line:
            beacons = []
        elif len(line) == 0:
            scanners.append(beacons)
        else:
            beacons.append([int(x) for x in line.split(',')])
    scanners.append(beacons)

    return scanners

def part1(input, debug=False):
    scanners = parse(input)
    pp.pprint(scanners)
    
    #print(f'Part 1 {input}: {len(grid.keys()) = }')

part1('example.txt')
# part1('input.txt')

# part2('example.txt')
# part2('input.txt')