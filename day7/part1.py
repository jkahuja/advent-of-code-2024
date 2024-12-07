import sys


calib_val = 0

for line in sys.stdin:
    line = line.strip()
    arr = line.split(':')
    target = int(arr[0])
    nums = arr[1].strip().split(' ')
    nums = [int(num) for num in nums]
    possible_ops = [] * len(nums)
    possible_totals = [nums[0] + nums[1], nums[0] * nums[1]]
    for i in range(2, len(nums)):
        len_possible_totals = len(possible_totals)
        for j in range(0, len_possible_totals):
            possible_totals.append(possible_totals[j] + nums[i])
            possible_totals[j] *= nums[i]
    for possible_total in possible_totals:
        if possible_total == target:
            calib_val += target
            break
        
        
print(calib_val)
