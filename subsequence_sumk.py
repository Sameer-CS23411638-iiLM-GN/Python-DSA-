nums = [5,9,1,1,2,10]
result = []
k = 9

def backtrack(index, total, subset):
    if total == k:
        result.append(subset.copy())
        return True
    elif total > k:
        return False
    if index >= len(nums):
        return False
    
    # pick
    subset.append(nums[index])
    pick = backtrack(index+1, total + nums[index], subset)
    if pick:
        return True
    
    # not pick
    subset.pop()
    not_pick = backtrack(index+1, total, subset)
    
    return not_pick

backtrack(0, 0, [])
print(result)