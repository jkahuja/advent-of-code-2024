import sys

safe_count = 0

for line in sys.stdin:
    nums = line.split()
    nums = [int(num) for num in nums]
    decreasing = None
    deviations = 0
    for i, num in enumerate(nums[:-1]):
        if num == nums[i + 1]:
            deviations += 1
            continue
        if num > nums[i + 1] and decreasing:
            deviations += 1
            continue
        if num < nums[i + 1] and decreasing is not None and not decreasing:
            deviations += 1
            continue
        decreasing = num < nums[i + 1]
        diff = abs(num - nums[i + 1])
        if diff == 0 or diff > 3:
            deviations += 1
            continue
    if deviations <= 1:
:       safe_count += 1
    else:
        print(deviations, nums)

print(safe_count)

