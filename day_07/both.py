#!/usr/bin/env python3

for file in ['example.txt', 'input.txt']:
    hpos = list(map(int, open(file).read().strip().split(',')))

    # Part 1
    fuels = {}
    for i in range(min(hpos), max(hpos)+1):
        fuel = sum([abs(h - i) for h in hpos])
        fuels[i] = fuel

    best_fuel_pos = min(fuels, key=fuels.get)
    print(f'Part 1 \'{file}\': lowest fuel position: {best_fuel_pos} fuel cost: {fuels[best_fuel_pos]}')

    # Part 2
    fuels = {}
    for i in range(min(hpos), max(hpos)+1):
        # triangular numbers = (N(N+1)) // 2
        fuel = sum([(abs(h-i) * (abs(h-i)+1)) // 2 for h in hpos])
        fuels[i] = fuel

    best_fuel_pos = min(fuels, key=fuels.get)
    print(f'Part 2 \'{file}\': lowest fuel position: {best_fuel_pos} fuel cost: {fuels[best_fuel_pos]}')