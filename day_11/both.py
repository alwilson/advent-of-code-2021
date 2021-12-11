#!/usr/bin/env python3

import time
import cv2
import numpy as np

import colorsys

def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))


i_height = 400
i_width = 400
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('output.mp4', fourcc, 10.0, (i_width, i_height))

grid = {}
width = 0
height = 0

def parse(input):
    global width, height, grid
    lines = [l.strip() for l in open(input)]
    width = len(lines[0])
    height = len(lines)
    for y, line in enumerate(lines):
        for x, octopus in enumerate(line):
            grid[(x,y)] = int(octopus)


def step():
    flashed = {}
    last_num_flashed = -1
    for loc in grid:
        grid[loc] += 1

    while last_num_flashed != len(flashed.keys()):
        # print_grid()
        last_num_flashed = len(flashed.keys())
        for loc in grid:
            x = loc[0]
            y = loc[1]

            if grid[loc] > 9 and loc not in flashed:
                flashed[loc] = True

                if (x+1,y  ) in grid: grid[x+1,y  ] += 1
                if (x-1,y  ) in grid: grid[x-1,y  ] += 1
                if (x+1,y+1) in grid: grid[x+1,y+1] += 1
                if (x-1,y-1) in grid: grid[x-1,y-1] += 1
                if (x  ,y+1) in grid: grid[x  ,y+1] += 1
                if (x  ,y-1) in grid: grid[x  ,y-1] += 1
                if (x-1,y+1) in grid: grid[x-1,y+1] += 1
                if (x+1,y-1) in grid: grid[x+1,y-1] += 1
    
    for loc in grid:
        if grid[loc] > 9:
            grid[loc] = 0

    return last_num_flashed


hue = 0
def print_grid():
    global hue
    # for y in range(height):
    #     for x in range(width):
    #         print(grid[(x,y)], end='')
    #     print()
    # print()

    image = np.zeros((i_height,i_width,3), np.uint8)

    for y in range(height):
        for x in range(width):
            lvl = grid[(x,y)]
            w = i_width // width 
            h = i_height// height

            if lvl == 0:
                color = hsv2rgb(hue, 0.7, 100.0/300.0)
            else:
                color = hsv2rgb(hue, 0.7, (lvl*lvl)/300.0)

            image[h*y+1:h*(y+1)-1, w*x+1:w*(x+1)-1] = color

    out.write(image)
    hue += 0.01


def part1(input, iter, debug=False):
    parse(input)

    total_flashes = 0
    if debug: print_grid()
    for _ in range(iter):
        total_flashes += step()
        if debug: print_grid()

    print(f'Part 1 {input}: {total_flashes = }')

def part2(input, debug=False):
    parse(input)

    total_octobuds = len(grid.keys())
    step_cnt = 1
    if debug: print_grid()
    while step() != total_octobuds:
        if debug: print_grid()
        step_cnt += 1
    if debug: 
        for _ in range(24):
            step()
            print_grid()
    print(f'Part 2 {input}: {step_cnt = }')
    out.release()

# part1('lil_example.txt', 3)
# part1('example.txt', 10)
# part1('example.txt', 100)
# part1('input.txt', 100)
# 
# part2('lil_example.txt')
# part2('example.txt')

part2('input.txt', True)


