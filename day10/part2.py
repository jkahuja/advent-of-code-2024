import sys

grid = []

for line in sys.stdin:
    line = line.strip()
    grid.append([int(ch) for ch in line])


trailheads = []

for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        if grid[i][j] == 0:
            trailheads.append((i, j))


def dfs(i, j, prev_num, seen):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
        return 0
    if grid[i][j] != prev_num + 1:
        return 0
    if grid[i][j] == 9:
        return 1

    return (
        dfs(i + 1, j, prev_num + 1, seen)
        + dfs(i - 1, j, prev_num + 1, seen)
        + dfs(i, j + 1, prev_num + 1, seen)
        + dfs(i, j - 1, prev_num + 1, seen)
    )


total = 0
for trailhead in trailheads:
    seen = set()
    val = dfs(trailhead[0], trailhead[1], -1, seen)
    total += val

print(total)

