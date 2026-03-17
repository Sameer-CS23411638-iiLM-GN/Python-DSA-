nums = [9,5,7]
result = []

def solve(ind,subset):
    if ind>=len(nums):
        result.append(subset.copy())
        return
    subset.append(nums[ind])
    solve(ind+1,subset)
    subset.pop()
    solve(ind+1,subset)
solve(0, [])   # function call

print(result)