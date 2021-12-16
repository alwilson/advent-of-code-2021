#!/usr/bin/env python3

import pprint as pp
import heapq

def parse(input):
    lines = [l.strip() for l in open(input)]
    return lines


def disect(hex_val, num_bits, debug=False):
    if debug: print(f'{num_bits = } {hex_val = :b}')

    calc = 0

    version = hex_val >> (num_bits-3)
    hex_val -= (version << (num_bits-3))
    num_bits -= 3
    if debug: print(f'{version = }')
    if debug: print(f'{num_bits = } {hex_val = :b}')
    
    typeID = hex_val >> (num_bits-3)
    hex_val = hex_val - (typeID << (num_bits-3))
    num_bits -= 3
    if debug: print(f'{typeID = }')
    if debug: print(f'{num_bits = } {hex_val = :b}')

    ver_sum = version    
    if typeID != 4:
        lenID = hex_val >> (num_bits-1)
        hex_val = hex_val - (lenID << (num_bits-1))
        num_bits -= 1
        if debug: print(f'{lenID = }')
        if debug: print(f'{num_bits = } {hex_val = :b}')

        calc_n = []
        if lenID:
            sub_len = hex_val >> (num_bits-11)
            hex_val = hex_val - (sub_len << (num_bits-11))
            num_bits -= 11
            if debug: print(f'{sub_len = } {num_bits = } {hex_val = :b}')

            while sub_len > 0:
                ver_sum_n, num_bits_n, hex_val, calc_i = disect(hex_val, num_bits, debug)
                calc_n.append(calc_i)
                sub_len -= 1
                ver_sum += ver_sum_n
                num_bits = num_bits_n
                if debug: print(f'{sub_len = } {ver_sum_n = } {num_bits_n = }')
        else:
            tot_len = hex_val >> (num_bits-15)
            hex_val = hex_val - (tot_len << (num_bits-15))
            num_bits -= 15
            if debug: print(f'{tot_len = } {num_bits = } {hex_val = :b}')

            while tot_len > 0:
                ver_sum_n, num_bits_n, hex_val, calc_i = disect(hex_val, num_bits, debug)
                calc_n.append(calc_i)
                tot_len -= num_bits - num_bits_n
                ver_sum += ver_sum_n
                num_bits = num_bits_n
                if debug: print(f'{ver_sum_n = } {num_bits_n = }')

        if debug: print(f'before {typeID = } {calc = } {calc_n = }')
        if typeID == 0:
            calc = sum(calc_n)
        if typeID == 1:
            calc = 1
            for c in calc_n:
                calc *= c
        if typeID == 2:
            calc = min(calc_n)
        if typeID == 3:
            calc = max(calc_n)
        if typeID == 5:
            calc = 1 if calc_n[0] > calc_n[1] else 0
        if typeID == 6:
            calc = 1 if calc_n[0] < calc_n[1] else 0
        if typeID == 7:
            calc = 1 if calc_n[0] == calc_n[1] else 0
        if debug: print(f'after  {typeID = } {calc = } {calc_n = }')

    if typeID == 4:
        number = 0
        while (hex_val & 0x1 << (num_bits-1)) and num_bits >= 5:
            num = hex_val >> (num_bits - 5)
            number <<= 4
            number += num & 0xF
            hex_val -= num << (num_bits - 5)
            num_bits -= 5

        num = hex_val >> (num_bits - 5)
        number <<= 4
        number += num & 0xF
        hex_val -= num << (num_bits - 5)
        num_bits -= 5
        if debug: print(number)
        if debug: print(f'{num_bits = } {hex_val = :b}')
        calc = number

    return ver_sum, num_bits, hex_val, calc


def part1(input, debug=False):
    hex_strs = parse(input)
    for hex_str in hex_strs:
        print(f'{hex_str = }')
        hex_val = int(hex_str,16)
        num_bits = len(hex_str)*4

        ver_sum, num_bits, hex_val, calc = disect(hex_val, num_bits)
        print(f'Part 1 {input}: {ver_sum = }')
        print(f'Part 2 {input}: {calc = }')

part1('example.txt')
part1('input.txt')