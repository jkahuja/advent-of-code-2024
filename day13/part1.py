import re
import sys

num_tokens = 0


def compute_tokens(a_delta, b_delta, prize_location):
    min_tokens = 500
    for i in range(0, 101):
        cur_location = [0, 0]
        num_a_moves = 0
        for k in range(0, i):
            if cur_location[0] + a_delta[0] > prize_location[0] and cur_location[1] + a_delta[1] > prize_location[1]:
                break
            cur_location[0] += a_delta[0]
            cur_location[1] += a_delta[1] 
            num_a_moves += 1
        if cur_location[0] == prize_location[0] and cur_location[1] == prize_location[1]:
            min_tokens = min(num_a_moves * 3, min_tokens)
            continue
        num_b_moves = 0
        while cur_location[0] + b_delta[0] <= prize_location[0] and cur_location[1] + b_delta[1] <= prize_location[1]:
            cur_location[0] += b_delta[0]
            cur_location[1] += b_delta[1]
            num_b_moves += 1
            if num_b_moves == 100:
                break
        
        if cur_location[0] == prize_location[0] and cur_location[1] == prize_location[1]:
            min_tokens = min(num_a_moves * 3 + num_b_moves, min_tokens)
    if min_tokens == 500:
        return None
    return min_tokens


for line in sys.stdin:
    line = line.strip()
    if "Button" in line:
        re_match = re.search("X\+(\d+), Y\+(\d+)", line)
        delta = (int(re_match.group(1)), int(re_match.group(2)))
        if "Button A" in line:
            a_delta = delta
        else:
            b_delta = delta
    if "Prize" in line:
        re_match = re.search("X=(\d+), Y=(\d+)", line)
        prize_location = (int(re_match.group(1)), int(re_match.group(2)))
    if not line:
        tokens = compute_tokens(a_delta, b_delta, prize_location)
        if tokens:
            num_tokens += tokens
tokens = compute_tokens(a_delta, b_delta, prize_location)
if tokens:
    num_tokens += tokens

           
print(num_tokens)
