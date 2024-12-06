import sys
from collections import defaultdict

words = []

for line in sys.stdin:
    words.append([ch for ch in line.strip()])


NEXT_CHAR_MAP = {'A': 'S'}

directions = [-1, 1]

a_positions = defaultdict(int)

def find_a_leg(i, j, ch, x_dir, y_dir):
    if i < 0 or i >= len(words) or j < 0 or j >= len(words[0]):
        return
    if words[i][j] != ch:
        return
    if ch == 'S' and words[i][j] == ch:
        a_positions[(i - x_dir, j - y_dir)] += 1
        return
    return find_a_leg(i + x_dir, j + y_dir, NEXT_CHAR_MAP[ch], x_dir, y_dir)

def find_legs(i, j):
    for dir_x in directions:
        for dir_y in directions:
            find_a_leg(i + dir_x, j + dir_y, 'A', dir_x, dir_y)
    return

for i in range(0, len(words)):
    for j in range(0, len(words[0])):
        if words[i][j] == 'M':
            find_legs(i, j)

total = 0
for pos, value in a_positions.items():
    if value == 2:
        total += 1

print(total)

