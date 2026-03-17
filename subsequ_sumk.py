# nums = [5,9,4]
# result = []
# target=k = 9
# def backtrack(index,total,subset):
#     if total == k:
#         result.append(subset.copy())
#         return
#     elif total>k:
#         return
#     if index>=len(nums):
#         return
#     subset.append(nums[index])
#     sum = total + nums[index]
#     backtrack(index+1,sum,subset)
#     e = subset.pop()
#     sum -= e
#     backtrack(index+1,sum,subset)

nums = [5,9,4]
result = []
k = 9

def backtrack(index, total, subset):
    if total == k:
        result.append(subset.copy())
        return
    elif total > k:
        return
    if index >= len(nums):
        return
    
    subset.append(nums[index])
    backtrack(index + 1, total + nums[index], subset)
    
    e = subset.pop()
    
    backtrack(index + 1, total, subset)

backtrack(0, 0, [])
print(result)