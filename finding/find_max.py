def find_max(nums):
    if not nums:
        return None

    max = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > max:
            max = nums[i]
    return max


