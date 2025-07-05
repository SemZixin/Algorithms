def find_min(nums):
    if not nums:
        return None

    min = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < min:
            min = nums[i]
    return min
