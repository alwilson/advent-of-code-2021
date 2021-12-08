#!/usr/bin/env python3

#         0 1 2 3 4 5 6 7 8 9
digits = [6,2,5,5,4,5,6,3,7,6]

entries = [l.strip() for l in open('input.txt')]

sum_1478 = 0
for e in entries:
    e_splits = e.split('|')
    output = e_splits[1].strip().split()
    for o in output:
        if len(o) in [digits[1], digits[4], digits[7], digits[8]]:
            sum_1478 += 1
print(f'{sum_1478}')
