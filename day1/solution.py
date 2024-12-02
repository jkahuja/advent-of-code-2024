import sys
from collections import defaultdict

list1 = []
location_id_count2 = defaultdict(int)

for line in sys.stdin:
    el1, el2 = line.split()
    list1.append(int(el1))
    location_id_count2[int(el2)] += 1     

total = 0
for num in list1:
    total += num * location_id_count2.get(num, 0)

print(total)
