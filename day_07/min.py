#!/usr/bin/env python3

hpos = open('input.txt').read().split(',')

fuel=tri_fuel=9**99
for i in range(9999):
    dist = [abs(int(h)-i) for h in hpos]
    fuel = min(fuel,(sum(dist)))
    tri_fuel = min(tri_fuel,sum([d*(d+1)//2 for d in dist]))

print(fuel,tri_fuel)