#!/usr/bin/env python3

def model_pop(ages, days):
    ages = ages.copy() # I don't know how to python globals and locals :P
    # print('initial: ', ages)
    for i in range(days):
        age0 = ages.pop(0)
        ages[6] += age0
        ages.append(age0)
    print('days: ', i+1, 'sum: ', sum(ages))

lines = [list(map(int, line.strip().split(','))) for line in open('input.txt')]

ages = [0] * 9
for age in lines[0]:
    ages[age] += 1

model_pop(ages, 80)
model_pop(ages, 256)