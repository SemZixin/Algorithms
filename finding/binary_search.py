nums = [9,8,7,6,5,4,3,2,1,0]
target = 8

def binary_search(nums, target):

    left = 0

    right = len(nums) - 1

    while left != right:
        
        mid = (left + right) // 2
        
        if nums[mid] == target:
            
            return mid
        
        elif nums[mid] > target:
            
            left = mid
            
        else:
            
            right = mid

    return right,left

print(binary_search(nums, target))
