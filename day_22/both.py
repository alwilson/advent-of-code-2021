#!/usr/bin/env python3

import functools
from Geometry3D import *

def parse(input):
    lines = [l.strip() for l in open(input)]
    return lines

def part1(input, debug=False):
    lines = parse(input)

    cubes = {}
    for line in lines:
        splits = line.split()
        on_off = splits[0]
        coords = splits[1].split(',')
        coords_ints = []
        for coor in coords:
            range_split = coor.split('=')[1].split('.')
            low = int(range_split[0])
            high = int(range_split[-1])

            if low < -50: low = -50
            if low > 50:  low = 50
            
            if high < -50: high = -50
            if high > 50:  high = 50

            if abs(low) == 50 and low == high: on_off = 'nope'
            coords_ints.append(low)
            coords_ints.append(high)

        for x in range(coords_ints[0], coords_ints[1]+1):
            for y in range(coords_ints[2], coords_ints[3]+1):
                for z in range(coords_ints[4], coords_ints[5]+1):
                    if on_off == 'on':
                        cubes[(x,y,z)] = True
                    if on_off == 'off':
                        if (x,y,z) in cubes:
                            del cubes[(x,y,z)]

        print(f'{on_off = } {coords_ints = }')
    print(len(cubes.keys()))

    # print(f'Part 1 {input}: {roll_total*min(p1_score,p2_score) = }')


def part2(input, debug=False):
    lines = parse(input)

    cubes = []
    for line in lines:
        splits = line.split()
        on_off = splits[0]
        coords = splits[1].split(',')
        cube = [1 if on_off == 'on' else -1]
        for coor in coords:
            range_split = coor.split('=')[1].split('.')
            low = int(range_split[0])
            high = int(range_split[-1])

            cube.append(low)
            cube.append(high)
        cubes.append(cube)

    intersections = []
    for cube in cubes:
        print(cube, intersections)

        new_intersections = []
        for ncube in intersections:
            min_x = max(cube[1],ncube[1])
            max_x = min(cube[2],ncube[2])
            min_y = max(cube[3],ncube[3])
            max_y = min(cube[4],ncube[4])
            min_z = max(cube[5],ncube[5])
            max_z = min(cube[6],ncube[6])
            intersects = min_x <= max_x and min_y <= max_y and min_z <= max_z
            print('\t', intersects, min_x, max_x, min_y, max_y, min_z, max_z)
            if intersects:
                if cube[0] == -1:
                    on_off = 1 if ncube[0] == -1 else -1
                else:
                    on_off = 1 if ncube[0] == -1 else -1
                new_intersections.append([on_off, min_x, max_x, min_y, max_y, min_z, max_z])
        
        if cube[0] == 1:
            new_intersections.append(cube)
        
        intersections += new_intersections

    print(cubes, intersections)


# part1('example2.txt')
# part1('input.txt')

part2('example.txt')
# part2('example3.txt')
# part2('input.txt')