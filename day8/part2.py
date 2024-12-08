import sys
from collections import defaultdict

grid = []

for line in sys.stdin:
    line = line.strip()
    grid.append([ch for ch in line])
    
freqs = defaultdict(list)


unique_locs = set()

for i in range(0, len(grid)):
    for j in range(0, len(grid[0])):
        if grid[i][j] == '.':
            continue
        freqs[grid[i][j]].append((i, j))
        unique_locs.add((i, j))


def is_valid(pos, coord):
    if coord == "row":
        upper = len(grid)
    else:
        upper = len(grid[0])
    return pos >= 0 and pos < upper

for freq, pos_list in freqs.items():
    for i in range(0, len(pos_list)): 
        for j in range(i + 1, len(pos_list)):
            row_diff = pos_list[i][0] - pos_list[j][0]
            col_diff = pos_list[i][1] - pos_list[j][1]

            k = 1
            while True:
                i_row_pos = pos_list[i][0] + k * row_diff
                i_col_pos = pos_list[i][1] + k * col_diff
                if not is_valid(i_row_pos, "row") or not is_valid(i_col_pos, "col"):
                    break
                unique_locs.add((i_row_pos, i_col_pos))
                k += 1
            k = 1
            while True:
                j_row_pos = pos_list[j][0] - k * row_diff
                j_col_pos = pos_list[j][1] - k * col_diff
                if not is_valid(j_row_pos, "row") or not is_valid(j_col_pos, "col"):
                    break
                unique_locs.add((j_row_pos, j_col_pos))
                k += 1

print(len(unique_locs))

