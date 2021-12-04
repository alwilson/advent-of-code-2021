#!/usr/bin/env python3

import sys
import pprint as pp

def dbg(msg = None):
    print(f"line {sys._getframe().f_back.f_lineno:4}: {msg if msg is not None else ''}")

lines = [line.strip() for line in open('input.txt')]

nums = [int(x) for x in lines[0].split(',')]

boards = []
for i, line in enumerate(lines):
    if line == '':
        board = []
        board.append([int(x) for x in lines[i+1].split()])
        board.append([int(x) for x in lines[i+2].split()])
        board.append([int(x) for x in lines[i+3].split()])
        board.append([int(x) for x in lines[i+4].split()])
        board.append([int(x) for x in lines[i+5].split()])
        boards.append(board)

# pp.pprint(boards)

def mark_boards(n):
    for board in boards:
        for row in board:
            for i, val in enumerate(row):
                if val == n:
                    row[i] = -1

def check_boards(n):
    for i, board in enumerate(boards):
        for row in board:
            if sum(row) == -5:
                return i
        
        for j in range(0,5):
            if sum([board[x][j] for x in range(0,5)]) == -5:
                return i

    return -1

for n in nums:
    mark_boards(n)
    bingo = check_boards(n)
    while bingo >= 0:
        # print(f'{len(boards)} boards left')
        if len(boards) == 1:
            print(f'last {bingo = }')
            print(boards[bingo])
            sum = 0
            for row in boards[bingo]:
                for val in row:
                    if val != -1:
                        sum += val
            print(f'{sum = }')
            print(f'{n = }')
            print(f'{sum * n = }')
            exit(0)
        else:
            # print(f'deleting {bingo}')
            boards.pop(bingo)
            bingo = check_boards(n)