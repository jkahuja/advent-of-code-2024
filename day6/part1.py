import sys

lab_map = []
unique_positions = set()


for line in sys.stdin:
    lab_map.append([ch for ch in line.strip()])

for i in range(0, len(lab_map)):
    for j in range(0, len(lab_map[i])):
        if lab_map[i][j] == "^":
            cur_i = i
            cur_j = j
            break

DIRECTION_FLIP = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}

i = cur_i
j = cur_j
dir_i = -1
dir_j = 0


while True:
    unique_positions.add((i, j))
    if i <= 0 or i >= len(lab_map) - 1:
        break
    if j <= 0 or j >= len(lab_map[0]) - 1:
        break

    if lab_map[i + dir_i][j + dir_j] == "#":
        dir_i, dir_j = DIRECTION_FLIP[(dir_i, dir_j)]
        i += dir_i
        j += dir_j
    else:
        i += dir_i
        j += dir_j


print(len(unique_positions))
