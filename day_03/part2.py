#!/usr/bin/env python3

import sys

def dbg(msg = None):
    print(f"line {sys._getframe().f_back.f_lineno:4}: {msg if msg is not None else ''}")

bits = [line.strip() for line in open('input.txt')]

# dbg(bits)

oxy_bits = []
co2_bits = []
for b in bits:
    if b[0] == '1':
        oxy_bits.append(b)
    else:
        co2_bits.append(b)

# print(oxy_bits)
# print(co2_bits)

# oxy
bit_pos0_l = [0] * len(bits[0])
bit_pos1_l = [0] * len(bits[0])
for i in range(1,len(bits[0])):
    bit_pos0 = 0
    bit_pos1 = 0
    for b in oxy_bits:
        if b[i] == '1':
            bit_pos1 += 1
        if b[i] == '0':
            bit_pos0 += 1
    new_oxy_bits = []
    # print(bit_pos0, bit_pos1)
    if bit_pos0 > bit_pos1:
        for b in oxy_bits:
            if b[i] == '0':
                new_oxy_bits.append(b)
    else:
        for b in oxy_bits:
            if b[i] == '1':
                new_oxy_bits.append(b)
    oxy_bits = new_oxy_bits
    if len(oxy_bits) == 1:
        # print('breaking', oxy_bits)
        break

# co2
for i in range(1,len(bits[0])):
    bit_pos0 = 0
    bit_pos1 = 0
    for b in co2_bits:
        if b[i] == '1':
            bit_pos1 += 1
        if b[i] == '0':
            bit_pos0 += 1
    new_co2_bits = []
    # print(bit_pos0, bit_pos1)
    if bit_pos1 >= bit_pos0:
        for b in co2_bits:
            if b[i] == '0':
                new_co2_bits.append(b)
    else:
        for b in co2_bits:
            if b[i] == '1':
                new_co2_bits.append(b)
    co2_bits = new_co2_bits
    if len(co2_bits) == 1:
        # print('breaking', co2_bits)
        break

# print(oxy_bits[0], int(oxy_bits[0], 2))
# print(co2_bits[0], int(co2_bits[0], 2))

dbg(f'{int(co2_bits[0], 2) * int(oxy_bits[0], 2) = }')