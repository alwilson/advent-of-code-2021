#!/usr/bin/env python3

with open('input.txt') as fd:
    bits = [line.strip() for line in fd]

# print(bits)

bit_pos0 = [0] * len(bits[0])
bit_pos1 = [0] * len(bits[0])
for b in bits:
    for i, c in enumerate(b):
        # print(i, c)
        if c == '1':
            bit_pos1[i] += 1
        if c == '0':
            bit_pos0[i] += 1

# print(bit_pos0)
# print(bit_pos1)

binary = ''
inverse = ''
for i, num_0 in enumerate(bit_pos0):
    if num_0 > bit_pos1[i]:
        binary += '1'
        inverse += '0'
    else:
        binary += '0'
        inverse += '1'

# print(binary, int(binary, 2))
# print(inverse, int(inverse, 2))

print(int(binary, 2) * int(inverse, 2))