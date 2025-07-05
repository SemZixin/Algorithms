nums = [3, 1, 4]

def insertion_sort(nums):
    
    for i in range(1, len(nums)):
        
        x = nums[i]

        
        for j in range(i, -1, -1):
            
            if j > 0 and x > nums[i - 1]:
                
                nums[j] = nums[j - 1]
                
            else:
                
                nums[j] = x
                
                break

    return nums

print(insertion_sort(nums))
