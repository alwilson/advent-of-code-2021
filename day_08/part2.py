#!/usr/bin/env python3

import pprint as pp

#         0 1 2 3 4 5 6 7 8 9
digits = [6,2,5,5,4,5,6,3,7,6]

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

#  0000
# 1    2
# 1    2
#  3333
# 4    5
# 4    5
#  6666


entries = [l.strip() for l in open('input.txt')]
# entries = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf']

total = 0
for e in entries:
    segments = [set('abcdefg') for i in range(7)]
    e_splits = e.split('|')
    pattern = e_splits[0].strip().split()
    output = e_splits[1].strip().split()
    for p in pattern:
        for d in [1, 4, 7, 8]:
            if len(p) == digits[d]:
                for seg in dig_seg[d]:
                    segments[seg] = segments[seg].intersection(p)

    # 1's are ambiguous, but form a known pair
    assert(segments[2] == segments[5])
    for si, seg in enumerate(segments):
        if si not in [2, 5]:
            segments[si] = seg.difference(segments[2])

    # we always know the top segment from 8
    assert(len(segments[0]) == 1)
    for si, seg in enumerate(segments):
        if si != 0:
            segments[si] = seg.difference(segments[0])
    
    # segments 1 and 3 are a known pair
    assert(segments[1] == segments[3])
    for si, seg in enumerate(segments):
        if si not in [1, 3]:
            segments[si] = seg.difference(segments[1])

    # 2,3, and 5 narrow down segments 3 and 6
    s235 = set('abcdefg')
    for p in pattern:
        if len(p) == 5:
            s235 = s235.intersection(p)
    s235 = s235.difference(segments[0])
    segments[3] = segments[3].intersection(s235)
    for si, seg in enumerate(segments):
        if si != 3:
            segments[si] = seg.difference(segments[3])
    segments[6] = segments[6].intersection(s235)
    for si, seg in enumerate(segments):
        if si != 6:
            segments[si] = seg.difference(segments[6])

    # 0,6,9 share 5 segments, 3 of which are known, and the other is a pair
    s069 = set('abcdefg')
    for p in pattern:
        if len(p) == 6:
            s069 = s069.intersection(p)
    s069 = s069.difference(segments[0])
    s069 = s069.difference(segments[1])
    s069 = s069.difference(segments[6])
    segments[2] = segments[2].difference(s069)
    for si, seg in enumerate(segments):
        if si != 2:
            segments[si] = seg.difference(segments[2])

    # Map segments back to their digits and accumulate to full number
    num = 0
    for o in output:
        o_segs = set()
        for c in o:
            for si, seg in enumerate(segments):
                if c in seg:
                    o_segs.add(si)
        for li, l in enumerate(dig_seg):
            if o_segs == set(l):
                num *= 10
                num += li
    total += num
print(total)