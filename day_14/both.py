#!/usr/bin/env python3

import pprint as pp

def parse(input):
    # chars is very lazy but complete set of characters
    chars = set()
    lines = [l.strip() for l in open(input)]
    template = lines[0]
    for c in template: chars.add(c)

    rules = {}
    for l in lines[2:]:
        if '->' in l:
            l_split = l.split()
            pair = l_split[0]
            for c in pair: chars.add(c)
            insert = l_split[2]
            for c in insert: chars.add(c)
            rules[pair] = insert

    return template, rules, chars


# A very simple string insertion to expand the template. DOES NOT SCALE! >:D
def insert_pairs(template, rules):
    new = ''
    for x in range(len(template)-1):
        new += template[x]
        pair = template[x:x+2]
        if pair in rules:
            new += rules[pair]
    
    new += template[-1]
    return new


def part1(input, debug=False):
    template = ''
    rules = {}
    chars = set()

    template, rules, chars = parse(input)

    if debug: print(template)
    if debug: pp.pprint(rules)

    for x in range(10):
        template = insert_pairs(template, rules)
    
    if debug: print(len(template))
    if debug: print(chars)

    sizes = [template.count(c) for c in chars]
    if debug: print(sizes)
    sizes.sort()
    size_diff = sizes[-1] - sizes[0]

    print(f'Part 1 {input}: {size_diff}')


# Take count of each pair and use rules to 'insert' to create next iteration of pairs
def update_pair_count(pair_count, rules):
    new_pair_count = {}
    for key, value in pair_count.items():
        if key not in rules:
            new_pair_count[key] = value
        else:
            insert = rules[key]
            # Split pair in two and pass on count (value)
            for pair in [key[0] + insert, insert + key[1]]:
                if pair not in new_pair_count:
                    new_pair_count[pair] = 0
                new_pair_count[pair] += value
    
    return new_pair_count


# Track count of each pair rather than an enourmous string, requires some math to get back to character count
def part2(input, iter, debug=False):
    template = ''
    rules = {}
    chars = set()

    template, rules, chars = parse(input)

    # Prime pair count dictionary
    pair_count = {}
    for x in range(len(template)-1):
        pair = template[x:x+2]
        if pair not in pair_count:
            pair_count[pair] = 0
        pair_count[pair] += 1

    if debug: print(template)
    if debug: pp.pprint(rules)

    for x in range(iter):
        pair_count = update_pair_count(pair_count, rules)
        if debug: print(x, pair_count)

    # Prime character count dictionary
    char_cnt = {}
    for c in chars:
        char_cnt[c] = 0

    # Count characters, which will be double the actual count except for edge characters
    for key, value in pair_count.items():
        char_cnt[key[0]] += value
        char_cnt[key[1]] += value
    
    # Account for missing start/end characters before halving
    char_cnt[template[0]] += 1
    char_cnt[template[-1]] += 1

    # Now divide all counts in half 
    for key, value in char_cnt.items():
        char_cnt[key] = value // 2

    if debug: print(char_cnt)

    # Get raw counts, sort, and find max/min difference
    sizes = list(char_cnt.values())
    sizes.sort()
    size_diff = sizes[-1] - sizes[0]

    print(f'Part 2 {input} @ {iter} steps: {size_diff}')

part1('example.txt')
part1('input.txt')

part2('example.txt', 10)
part2('example.txt', 40)
part2('input.txt', 10)
part2('input.txt', 40)