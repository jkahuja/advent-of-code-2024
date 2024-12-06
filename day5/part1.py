import sys

rules = []
page_arr = []

for line in sys.stdin:
    if "|" in line:
        rules.append(line.strip().split("|"))
    elif line.strip():
        page_arr.append(line.strip().split(","))
        # arr = line.split(',')
        # for i, page in enumerate(arr):
        #    page_arr[-1][page] = i

total = 0

for rule in rules:
    first_page = rule[0]
    second_page = rule[1]

    def does_match(seq):
        try:
            first_pos = seq.index(first_page)
            second_pos = seq.index(second_page)
        except ValueError:
            return True
        return first_pos < second_pos

    page_arr[:] = [seq for seq in page_arr if does_match(seq)]

total = 0
for seq in page_arr:
    total += int(seq[int(len(seq) / 2)])

print(total)
