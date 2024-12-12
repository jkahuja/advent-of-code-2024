import sys

string = sys.stdin.readline().strip()

stones_arr = string.split(" ")

new_stones_arr = []

for i in range(0, 25):
    for stone in stones_arr:
        if stone == '0':
            new_stones_arr.append('1')
        elif len(stone) % 2 == 0:
            split_point = int(len(stone) / 2)
            new_stones_arr.append(str(int(stone[:split_point])))
            new_stones_arr.append(str(int(stone[split_point:])))
        else:
            new_stones_arr.append(str(int(stone) * 2024))
    stones_arr = new_stones_arr[:] 
    new_stones_arr = [] 

print(len(stones_arr))
