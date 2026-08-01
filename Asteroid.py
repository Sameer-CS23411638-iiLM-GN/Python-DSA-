nums = [4, 7, 1, 1, 2, -3, -7, 17, 15, -18, -19]

stack = []

for i in range(len(nums)):
    if nums[i] > 0:
        stack.append(nums[i])
    else:
        while stack and stack[-1] > 0 and stack[-1] < abs(nums[i]):
            stack.pop()
        
        if stack and stack[-1] == abs(nums[i]):
            stack.pop()
        
        elif not stack or stack[-1] < 0:
            stack.append(nums[i])

print(stack)

Stack = []
for i in range(len(nums)):
    if nums[i]>0:
        stack.append(nums[i])
    else:
        while stack and stack[-1] > 0 and stack[-1] < abs(nums[i]):
            stack.pop()
        if stack and stack[-1] == abs(nums[i]):
            stack.pop()
        elif not stack or stack[-1] < 0:
            stack.append(nums[i])
print(stack)
