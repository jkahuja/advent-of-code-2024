import re
import sys

num_tokens = 0


def compute_tokens(a_delta, b_delta, prize_location):
    min_tokens = None
    for i in range(100000000, 10000000000000):
        cur_location = [0, 0]
        cur_location[0] = cur_location[0] + i * a_delta[0]
        cur_location[1] = cur_location[1] + i * a_delta[1]
        if cur_location[0] == prize_location[0] and cur_location[1] == prize_location[1]:
            if min_tokens is None:
                min_tokens = i * 3
            else:
                min_tokens = min(i * 3, min_tokens)
            continue
        for j in range(100000000, 10000000000000):
            cur_location[0] = cur_location[0] + j * a_delta[0]
            cur_location[1] = cur_location[1] + j * a_delta[1]
            if cur_location[0] == prize_location[0] and cur_location[1] == prize_location[1]:
                if min_tokens is None:
                    min_tokens = num_a_moves * 3 + num_b_moves
                else:
                    min_tokens = min(num_a_moves * 3 + num_b_moves, min_tokens)
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
        prize_location = (int(re_match.group(1)) + 10000000000000, int(re_match.group(2)) + 10000000000000)
    if not line:
        tokens = compute_tokens(a_delta, b_delta, prize_location)
        if tokens:
            num_tokens += tokens
tokens = compute_tokens(a_delta, b_delta, prize_location)
if tokens:
    num_tokens += tokens

           
print(num_tokens)

