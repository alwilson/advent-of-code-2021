#!/usr/bin/env python3

ages = [0]*9
for i in open('input.txt').read().split(','):
    ages[int(i)] += 1

for d in range(256):
    ages = ages[1:] + ages[:1]
    ages[6] += ages[8]
    d in [79, 255] and print(sum(ages))