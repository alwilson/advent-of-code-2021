#!/usr/bin/env python3

hmap = [l.strip() for l in open('input.txt')]

hmap_d = {}
for y, row in enumerate(hmap):
    for x, c in enumerate(row):
        hmap_d[(x,y)] = int(c)

hmap_d_seen = {}

def explore(x,y):
    loc = (x,y)
    # Stop searching at the edges
    # or what's already been seen
    if loc in hmap_d_seen or \
       loc not in hmap_d  or \
       hmap_d[loc] == 9:
        return 0
    hmap_d_seen[loc] = 1

    # Return sum of this point and
    # the exploration of neighbors
    return 1 + explore(x+1,y  ) + \
               explore(x-1,y  ) + \
               explore(x  ,y+1) + \
               explore(x  ,y-1)

risk_lvl = 0
basins = []
# Find the low points and basin sizes
for y, row in enumerate(hmap):
    for x, c in enumerate(row):
        loc = (x,y)
        low_pnt = True
        
        nbr = (x+1,y)
        for nbr in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
            if nbr in hmap_d and hmap_d[loc] >= hmap_d[nbr]:
                low_pnt = False

        if low_pnt:
            risk_lvl += hmap_d[loc] + 1
            basin_size = explore(x,y)
            basins.append(basin_size)

print('Part 1: ', risk_lvl)

basins.sort()
print('Part 2: ', basins.pop() * basins.pop() * basins.pop())