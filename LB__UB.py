nums = [1,3,4,5,8,9,14,15,19,20,21]

target = 1

#lower bound
n = len(nums)
lb = n
low = 0
high = n - 1
while low <= high:
    mid = (low + high)//2
    if nums[mid] >= target:
        lb = mid
        high = mid - 1
    else:
        low = mid + 1
print(lb)

#upper bound
n = len(nums)
ub = n
low = 0
high = n - 1
while low <= high:
    mid = (low + high)//2
    if nums[mid] > target:
        ub = mid
        high = mid - 1
    else:
        low = mid + 1
print(ub)