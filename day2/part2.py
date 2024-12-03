import copy
import sys

safe_count = 0

def is_safe(nums):
    decreasing = None
    for i, num in enumerate(nums[:-1]):
        if num == nums[i + 1]:
            return False
        if num > nums[i + 1] and decreasing:
            return False
        if num < nums[i + 1] and decreasing is not None and not decreasing:
            return False
        decreasing = num < nums[i + 1]
        diff = abs(num - nums[i + 1])
        if diff == 0 or diff > 3:
            return False
    return True


for line in sys.stdin:
    nums = line.split()
    nums = [int(num) for num in nums]
    if is_safe(nums):
        safe_count += 1
    else:
        for i in range(0, len(nums)):
            new_nums = copy.deepcopy(nums)
            del new_nums[i]
            if is_safe(new_nums):
                safe_count += 1
                break
            

print(safe_count)

