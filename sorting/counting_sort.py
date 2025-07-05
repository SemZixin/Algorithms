nums = [2,4,1,3,5,8,6,7]

def counting_sort(nums):
    lst = len(nums)*[0]
    for i in range(len(nums)):
        index = nums[i] - 1
        lst[index] += 1
    output = []
    for j in range(len(nums), 0, -1):
        for x in range(lst[j - 1]):
            output.append(j)

    return output

print(counting_sort(nums))
