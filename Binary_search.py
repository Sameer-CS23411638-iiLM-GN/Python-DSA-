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

#search insert position
nums = [1,3,4,5,8,9,14,15,19,20,21]
target = 13
n = len(nums)
lb = n
low = 0
high = n-1
while low<=high:
    mid = (low+high)//2
    if nums[mid]>=target:
        lb = mid
        high = mid-1
    else:
        low = mid+1
print(lb) 

#ceil the floor
nums = [3,4,4,4,8,9,9,10,12,12,14,15]
target = 6
n = len(nums)
floor = -1
ceil = -1
low = 0
high = n-1
while low<=high:
    mid = (low+high)//2
    if nums[mid]==target:
       print(nums[mid],nums[mid])
    elif nums[mid]>target:
        ceil = nums[mid]
        high = mid-1
    else:
        floor = nums[mid]
        low = mid+1
print(floor,ceil)

#first and last occurrence

nums = [3,4,4,4,8,9,9,10,12,12,14,15]
#brute force approach
target = 4
first = -1
last = -1
n = len(nums)
for i in range(0,n):
    if nums[i]==target:
        if first==-1:
            first = i
        last = i
print(first, last)

#optimized approach - sorted array use binary search
nums = [3,4,4,4,8,9,9,10,12,12,14,15]
target = 3
def lower_bound(nums,target):
    n = len(nums)
    lb = n
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if nums[mid]>=target:
            lb = mid
            high = mid-1
        else:
            low = mid+1
    return lb
def upper_bound(nums,target):
    n = len(nums)
    ub = -1
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if nums[mid]<=target:
            ub = mid
            low = mid+1
        else:
            high = mid-1
    return ub
lb = lower_bound(nums,target)
ub = upper_bound(nums,target)
if lb==len(nums) or nums[lb]!=target:
    print(-1,-1)

#seach in rotate sorted array - 1
nums = [11,12,15,18,20,21]
n = len(nums)
target = 15
for i in range(0,n):
    if nums[i]==target:
        print(i)
print(-1)

#optimal
nums = [17,18,20,13,4,5,7,8,10,11,13,14,16]
target = 13
#identify the sorted part
#check if the target lies in the sorted part or not
#if not high = mid-1 else low = mid+1
n = len(nums)
low = 0
high = n-1  
while low<=high:
    mid = (low+high)//2
    if nums[mid]==target:
        print(mid)
    if nums[mid]<=nums[high]:
        if nums[mid]<=target<=nums[high]:
            low = mid+1
        else:
            high = mid-1
    else:
        if nums[low]<=target<=nums[mid]:
            high = mid-1
        else:
            low = mid+1
print(-1)

#search in rotated sorted array - 2
nums = [10,11,11,12,12,13,13,13,1,2,3,4]
target = 11
n = len(nums)
low = 0
high = n-1  
while low<=high:
    mid = (low+high)//2
    if nums[mid]==target:
        print(True)
    if nums[low]==nums[mid]==nums[high]:
        low+=1
        high-=1
        continue
    if nums[mid]<=nums[high]:
        if nums[mid]<=target<=nums[high]:
            low = mid+1
        else:
            high = mid-1
    else:
        if nums[low]<=target<=nums[mid]:
            high = mid-1
        else:
            low = mid+1
print(False)

#find minimum in rotated sorted array
nums = [4,5,6,7,0,1,2]
n = len(nums)
minimum = nums[0]
for num in nums:
    minimum = min(minimum, num)

print(minimum)

#optimal approach
n = len(nums)
low = 0
high = n-1
mini = float("inf")
while low<=high:
    mid = (low+high)//2
    if nums[mid]<=nums[high]:
        mini = min(mini, nums[mid])
        high = mid-1
    else:
        mini = min(mini, nums[low])
        low = mid+1

print(mini)

