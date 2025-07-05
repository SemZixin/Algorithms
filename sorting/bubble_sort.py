nums = [3, 6, 4, 1, 5, 8, 2, 7, 9]

def bubble_sort(nums):
    
    for i in range(len(nums)):
        
        for j in range(len(nums) - 1):
            
            if nums[j] < nums[j + 1]:
                
                n = nums[j]
                
                nums[j] = nums[j + 1]
                
                nums[j + 1] = n
                
    return nums

print(bubble_sort(nums))
