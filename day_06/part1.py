#!/usr/bin/env python3

import sys
import pprint as pp

def dbg(msg = None):
    print(f"line {sys._getframe().f_back.f_lineno:4}: {msg if msg is not None else ''}")

lines = [line.strip() for line in open('input.txt')]

ages = [0] * 9
for age in lines[0].split(','):
    ages[int(age)] += 1

# print('initial: ', ages)

days = 80
for i in range(days):
    new_ages = [0] * 9
    for age_i, age in enumerate(ages):
        if age_i == 0:
            new_ages[6] += age
            new_ages[8] += age
        else:
            new_ages[age_i-1] += age
    ages = new_ages
    # print(i+1, ages, sum(ages))
print('days: ', i+1, 'sum: ', sum(ages))