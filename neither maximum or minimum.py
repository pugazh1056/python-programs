def maximumorminimum(nums):
    nums.sort()
    if len(nums)>2:
        return (nums[1])
    else:
        return -1