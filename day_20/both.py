#!/usr/bin/env python3

def parse(input):
    lines = [l.strip() for l in open(input)]
    next_state = [c for c in lines[0]]

    grid = {}
    for y, line in enumerate(lines[2:]):
        for x, c in enumerate(line):
            if c == '#':
                grid[(x,y)] = True

    return next_state, grid

def print_grid(grid):
    x_min = min([x[0] for x in grid.keys()])
    x_max = max([x[0] for x in grid.keys()])
    y_min = min([x[1] for x in grid.keys()])
    y_max = max([x[1] for x in grid.keys()])

    print()
    for y in range(y_min, y_max+1):
        for x in range(x_min, x_max+1):
            if (x,y) in grid:
                print('#', end='')
                # print('█', end='')
            else:
                print('.', end='')
        print()
    print()


def update_grid(grid, next_state, add_halo):
    x_min = min([x[0] for x in grid.keys()])
    x_max = max([x[0] for x in grid.keys()])
    y_min = min([x[1] for x in grid.keys()])
    y_max = max([x[1] for x in grid.keys()])

    if add_halo == 0:
        x_min -= 5
        x_max += 3
        y_min -= 5
        y_max += 3
    if add_halo == 1:
        #x_min -= 2
        x_max -= 2
        #y_min -= 2
        y_max -= 2
    if add_halo == 2:
        x_min -= 2
        #x_max -= 2
        y_min -= 2
        #y_max -= 2

    new_grid = {}
    for y in range(y_min, y_max+1):
        for x in range(x_min, x_max+1):
            idx = 0
            for pos in [(x,y  ), (x+1,y  ), (x+2,y  ),
                        (x,y+1), (x+1,y+1), (x+2,y+1),
                        (x,y+2), (x+1,y+2), (x+2,y+2)]:
                if pos in grid:
                    # print('#', end='')
                    idx <<= 1
                    idx += 1
                else:
                    # print('.', end='')
                    idx <<= 1
            # print(' - ', idx)
            if next_state[idx] == '#':
                new_grid[(x+1,y+1)] = True

    return new_grid


def part1(input, debug=False):
    next_state, grid = parse(input)

    if next_state[0] == '#':
        halo = 0
    else:
        halo = 2

    if debug: print_grid(grid)
    for _ in range(2):
        grid = update_grid(grid, next_state, halo)
        if next_state[0] == '#': halo ^= 1
    if debug: print_grid(grid)

    print(f'Part 1 {input}: {len(grid.keys()) = }')

def part2(input, debug=False):
    next_state, grid = parse(input)

    if next_state[0] == '#':
        halo = 0
    else:
        halo = 2

    if debug: print_grid(grid)
    for _ in range(50):
        grid = update_grid(grid, next_state, halo)
        if next_state[0] == '#': halo ^= 1
    if debug: print_grid(grid)

    print(f'Part 1 {input}: {len(grid.keys()) = }')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')