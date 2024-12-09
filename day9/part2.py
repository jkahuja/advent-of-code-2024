import sys

string = sys.stdin.readline().strip()

disc_space_rep = []

file_id = 0

is_file = True
for rep in string:
    symbol_to_add = str(file_id) if is_file else '.'
    for i in range(0, int(rep)):
        disc_space_rep.append(symbol_to_add)
    if is_file:
        file_id += 1
    is_file = not is_file


free_spaces = []
i = 0
while i < len(disc_space_rep):
    while i < len(disc_space_rep) and disc_space_rep[i] != '.':
        i += 1
    j = i
    free_space_size = 0
    while j < len(disc_space_rep) and disc_space_rep[j] == '.':
        j += 1
        free_space_size += 1
    if free_space_size > 0:
        free_spaces.append((i, free_space_size))
    i += free_space_size

j = len(disc_space_rep) - 1
while disc_space_rep[j] == '.':
    j -= 1

while j >= 0:
    file_size = disc_space_rep.count(disc_space_rep[j])
    for r, free_space in enumerate(free_spaces):
        if free_space[1] >= file_size and free_space[0] < j - file_size:
            i = free_space[0]
            for k in range(j, j - file_size, -1):
                disc_space_rep[i], disc_space_rep[k] = disc_space_rep[k], disc_space_rep[i]
                i += 1
            free_spaces[r] = (free_space[0] + file_size, free_space[1] - file_size)
            break
    j -= file_size
    while disc_space_rep[j] == '.':
        j -= 1

checksum = 0

for i, ch in enumerate(disc_space_rep):
    if ch.isdigit():
        checksum += int(ch) * i
    
print(checksum) 

