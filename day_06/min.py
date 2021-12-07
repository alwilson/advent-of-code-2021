#!/usr/bin/env python3

for days in [80, 256]:
    ages = [0]*9
    for i in open('input.txt').read().split(','):
        ages[int(i)] += 1

    for _ in [0]*days:
        ages = ages[1:] + ages[:1]
        ages[6] += ages[8]
    print(sum(ages))