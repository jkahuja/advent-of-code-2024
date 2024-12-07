import sys
import copy
from collections import defaultdict

lab_map = []


for line in sys.stdin:
    lab_map.append([ch for ch in line.strip()])

for i in range(0, len(lab_map)):
    for j in range(0, len(lab_map[i])):
        if lab_map[i][j] == "^":
            cur_i = i
            cur_j = j
            break

DIRECTION_FLIP = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}


n_obstructions = 0

for m in range(0, len(lab_map)):
    for n in range(0, len(lab_map[i])):
        if lab_map[m][n] != '.':
            continue
        map_copy = copy.deepcopy(lab_map)
        map_copy[m][n] = '#'
        
        seen_places = set()
        i = cur_i
        j = cur_j
        dir_i = -1
        dir_j = 0

        while True:
            if (i, j, dir_i, dir_j) in seen_places:
                n_obstructions += 1
                break
            seen_places.add((i, j, dir_i, dir_j))
            if i <= 0 or i >= len(map_copy) - 1:
                break
            if j <= 0 or j >= len(map_copy[0]) - 1:
                break

            if map_copy[i + dir_i][j + dir_j] == "#":
                dir_i, dir_j = DIRECTION_FLIP[(dir_i, dir_j)]
                i += dir_i
                j += dir_j
            else:
                i += dir_i
                j += dir_j


print(n_obstructions)
