#!/usr/bin/env python3

with open('./input.txt') as fd:
    depths = [int(line) for line in fd]

cnt = 0
for d_i, d in enumerate(depths[:-3]):
    if depths[d_i+3] > d:
        cnt += 1

print(cnt)
