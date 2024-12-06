import re
import sys


string = sys.stdin.readline()

regex_matches = re.findall("mul\((\d+),(\d+)\)", string)
total = 0
for regex_match in regex_matches:
    total += int(regex_match[0]) * int(regex_match[1])
    
print(total)
