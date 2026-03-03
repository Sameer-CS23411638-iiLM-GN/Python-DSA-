nums = [1,3,4,5,8,9,14,15,19,20,21]

#iterative approach

def binarySearch(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
target = 5
print(binarySearch(nums, target))

#recursive approach
def binarySearch(nums, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binarySearch(nums, mid + 1, high)
    else:
        return binarySearch(nums, low, mid - 1)