import sys
from collections import defaultdict

rules = []
after_rules = defaultdict(list)
page_arr = []

for line in sys.stdin:
    line = line.strip()
    if "|" in line:
        arr = line.split("|")
        after_rules[arr[1]].append(arr[0])
    elif line.strip():
        page_arr.append(line.split(","))

seqs_to_count = []

for seq in page_arr:

    def do_the_sort(page):
        num_before_this_page = 0
        for other_page in seq:
            if page == other_page:
                continue
            if other_page in after_rules[page]:
                num_before_this_page += 1
        return num_before_this_page

    new_seq = sorted(seq, key=do_the_sort)
    if seq != new_seq:
        seqs_to_count.append(new_seq)

total = 0

for seq in seqs_to_count:
    total += int(seq[int(len(seq) / 2)])

print(total)
