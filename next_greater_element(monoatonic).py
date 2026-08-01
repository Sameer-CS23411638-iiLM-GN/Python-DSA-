nums = [19, 4, 2, 11, 6, 5, 3, 10]
n = len(nums)

ans = [-1] * n  # initialize with -1

for i in range(n):
    for j in range(i + 1, n):
        if nums[j] > nums[i]:
            ans[i] = nums[j]
            break

print(ans)

#optimal
nums = [19, 4, 2, 11, 6, 5, 3, 10]
n = len(nums)

ans = [-1] * n
stack = []

for i in range(n - 1, -1, -1):
    while stack and stack[-1] <= nums[i]:
        stack.pop()
    
    if stack:
        ans[i] = stack[-1]
    
    stack.append(nums[i])

print(ans)
