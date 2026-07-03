#binary search - iterative approach
nums=[2,4,6,7,9,11,18,19]
target = 13
def binarysearch(nums,target):
    n = len(nums)
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            low = mid+1
        else:
            high = mid-1
    return -1

result = binarysearch(nums, target)
print(result)

#recursion approach
nums=[2,4,6,7,9,11,18,19]
target = 13
def binarysearch(nums,low,high):
    if low>high:
        return -1
    mid = (low+high)//2
    if nums[mid]==target:
        return mid
    elif nums[mid]<target:
        return binarysearch(nums,mid+1,high)
    else:
        return binarysearch(nums,low,mid-1)

#Lower Bound[smallest index such that nums[i]>=target]
nums=[2,4,6,7,9,11,18,19]
target = 15
n = len(nums)
lb = n
low = 0
high = n - 1
while low<=high:
    mid=(low+high)//2
    if nums[mid]>=target:
        lb=mid
        high=mid-1
    else:
        low=mid+1
print(lb)

#upper bound

nums=[2,4,6,7,9,11,18,19]
n = len(nums)
UB = 0
low = 0
high = n - 1
while low<=high:
    mid=(low+high)//2
    if nums[mid]>target:
        UB = mid
        high = mid-1
    else:
        low = mid+1
print(UB)