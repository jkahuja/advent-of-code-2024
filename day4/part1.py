import sys

words = []

for line in sys.stdin:
    words.append([ch for ch in line.strip()])

total = 0

NEXT_CHAR_MAP = {'M': 'A', 'A': 'S'}

def examine_candidate_recursive(i, j, ch, i_change, j_change):
    if i < 0 or i >= len(words) or j < 0 or j >= len(words[0]):
        return 0
    if words[i][j] != ch:
        return 0
    if ch == 'S' and words[i][j] == ch:
        return 1
    return examine_candidate_recursive(i + i_change, j + j_change, NEXT_CHAR_MAP[ch], i_change, j_change)

def examine_candidate(i, j, ch):
    return examine_candidate_recursive(i - 1, j, ch, -1, 0) + examine_candidate_recursive(i + 1, j, ch, 1, 0) + examine_candidate_recursive(i, j - 1, ch, 0, -1) + examine_candidate_recursive(i, j + 1, ch, 0, 1) + examine_candidate_recursive(i - 1, j - 1, ch, -1, -1) + examine_candidate_recursive(i + 1, j + 1, ch, 1, 1) + examine_candidate_recursive(i + 1, j - 1, ch, 1, -1) + examine_candidate_recursive(i - 1, j + 1, ch, -1, 1)

for i in range(0, len(words)):
    for j in range(0, len(words[0])):
        if words[i][j] == 'X':
            total += examine_candidate(i, j, 'M')

print(total)
