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

i = 0
j = len(disc_space_rep) - 1

while disc_space_rep[i] != '.':
    i += 1 
while disc_space_rep[j] == '.':
    j -= 1


while i < j and i < len(disc_space_rep) and j >= 0:
    disc_space_rep[i], disc_space_rep[j] = disc_space_rep[j], disc_space_rep[i]
    while disc_space_rep[i] != '.':
        i += 1 
    while disc_space_rep[j] == '.':
        j -= 1

print("".join(disc_space_rep))

checksum = 0

for i, ch in enumerate(disc_space_rep):
    if ch.isdigit():
        checksum += int(ch) * i
    
print(checksum) 
