import sys

safe_count = 0

for line in sys.stdin:
    nums = line.split()
    nums = [int(num) for num in nums]
    decreasing = None
    is_safe = True
    for i, num in enumerate(nums[:-1]):
        if num == nums[i + 1]:
            is_safe = False
            break
        if num > nums[i + 1] and decreasing:
            is_safe = False
            break
        if num < nums[i + 1] and decreasing is not None and not decreasing:
            is_safe = False
            break
        decreasing = num < nums[i + 1]
        diff = abs(num - nums[i + 1])
        if diff == 0 or diff > 3:
            is_safe = False
            break
    if is_safe:
        print(nums, is_safe)
        safe_count += 1

print(safe_count)
