import re
import sys


string = sys.stdin.readline()

def compute_total_for_substring(substring):
    regex_matches = re.findall("mul\((\d+),(\d+)\)", substring)

    total = 0
    for regex_match in regex_matches:
        total += int(regex_match[0]) * int(regex_match[1])
    return total


first_dont = string.find("don't()")
first_muls = string[:first_dont]

total = compute_total_for_substring(first_muls)

string = string[first_dont + 7:]

dont_index = None


while (do_index := string.find("do()")) != -1 and dont_index != -1:
    dont_index = string.find("don't()")
    substring = string[do_index:dont_index] 
    total += compute_total_for_substring(substring)
    string = string[dont_index + 7:]

print(total)
