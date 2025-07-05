def partition(arr, l, p):
    pivot = p
    left = l
    right = p - 1
    while left <= right:
        if arr[left] < arr[pivot]:
            left += 1
        elif arr[right] > arr[pivot]:
            right -= 1
        else:
            arr[right], arr[left] = arr[left], arr[right]
            left += 1
            right -= 1
    arr[left], arr[p] = arr[p], arr[left]
    return left

def quick_sort(arr, left, right):
    left = left
    right = right
    if left <= right:
        p = partition(arr, left, right)
        quick_sort(arr, left, p - 1)
        quick_sort(arr, p + 1, right)
    return arr

nums = [3, 4, 6, 1, 2, 4, 7, 5]

print(quick_sort(nums, 0, len(nums) - 1))
