#!/usr/bin/env python3

lines = [l.strip() for l in open('input.txt')]

unexpected = ''
incomplete_scores = []
for l in lines:
    stack = []
    corrupted = False
    for c in l:
        if c in '(': stack.append(')')
        if c in '{': stack.append('}')
        if c in '[': stack.append(']')
        if c in '<': stack.append('>')
        
        if c in ')}]>':
            expected = stack.pop()
            if c != expected:
                # print(f'Expected {expected}, but found {c} instead.')
                unexpected += c
                corrupted = True
                break
    if not corrupted:
        score = 0
        # print(''.join(stack[::-1]))
        for s in stack[::-1]:
            score *= 5
            if s in ')': score += 1
            if s in ']': score += 2
            if s in '}': score += 3
            if s in '>': score += 4
        # print(score)
        incomplete_scores.append(score)

print('Part 1: ', unexpected.count(')') * 3 + unexpected.count(']') * 57 + unexpected.count('}') * 1197 + unexpected.count('>') * 25137)

incomplete_scores.sort()
middle_score = len(incomplete_scores) // 2
print('Part 2: ', incomplete_scores[middle_score])