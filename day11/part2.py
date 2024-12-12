import sys

string = sys.stdin.readline().strip()

stones_arr = string.split(" ")

def get_new_stones_arr(stones_arr):
    for stone in stones_arr:
        if stone == '0':
            yield '1'
        elif len(stone) % 2 == 0:
            split_point = int(len(stone) / 2)
            yield str(int(stone[:split_point]))
            yield str(int(stone[split_point:]))
        else:
            yield str(int(stone) * 2024)


for i in range(0, 35):
    stones_arr = get_new_stones_arr(stones_arr)

print(len(list(stones_arr)))

