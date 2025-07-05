nums = [2,4,1,3,5,8,6,7]

def find_max_index(nums,start):
    maximum = start
    for j in range(start, len(nums)):
        if nums[j] > nums[maximum]:
            maximum = j
    return maximum

def selection_sort(nums):
    for i in range(len(nums)):
        fst = nums[i]
        maximum = find_max_index(nums, i)
        nums[i] = nums[maximum]
        nums[maximum] = fst

    return nums

print(selection_sort(nums))
