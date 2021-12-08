#!/usr/bin/env python3
# Describes day 8 7-segment display problem in Z3 constraints:
# - Each segment's position is tracked as an Int and is distinct
# - Each signal pattern corresponds to a digit 0-9 and is distinct
# - Each pattern's segments could be any of the segments of the digits
#   of the same length _and_ that match the pattern's digit

from z3 import *

#  00
# 1  2
#  33
# 4  5
#  66

# List segments belonging to each digit
dig_seg = [[0,1,2,4,5,6],
           [2,5],
           [0,2,3,4,6],
           [0,2,3,5,6],
           [1,2,3,5],
           [0,1,3,5,6],
           [0,1,3,4,5,6],
           [0,2,5],
           [0,1,2,3,4,5,6],
           [0,1,2,3,5,6]]

entries = [l.strip() for l in open('input.txt')]

total = 0
for entry in entries:
    s = Solver()

    # Track position of each segment, which must be unique
    segments = {}
    for c in 'abcdefg': segments[c] = Int(f'{c}')
    s.add(Distinct(list(segments.values())))

    # Parse digit patterns and output
    e_splits = entry.split('|')
    patterns = e_splits[0].strip().split()
    output  = e_splits[1].strip().split()

    # Each digit pattern corresponds to a single digit and is unique
    patterns_c = [Int(f'{i}') for i in patterns]
    s.add(Distinct(patterns_c))
    for p_i, pattern in enumerate(patterns):
        for c in pattern:
            seg_options = []
            for digit, seg in enumerate(dig_seg):
                # This pattern is the same length as these digits
                if len(pattern) == len(seg):
                    # If this pattern is this digit then this segement would be one that digit's segments
                    seg_options.append(And(patterns_c[p_i] == digit, Or([segments[c] == i for i in seg])) )
            # One of these will be true and the distinct/unique constraint prevents overlap
            s.add(Or(seg_options))

    # Test if there's a solution
    ret = s.check()
    if ret == sat:
        m = s.model()

        # Map segments back to their digits and accumulate to full number
        num = 0
        for digit in output:
            segs = set()
            # Lookup segments for this scrambled digit
            for c in digit:
                segs.add(m[segments[c]].as_long())
            # Which digit maps to those segments
            for digit_val, seg_list in enumerate(dig_seg):
                if segs == set(seg_list):
                    num = num * 10 + digit_val
        total += num
    else:
        print(ret)
        exit(-1)
print(total)