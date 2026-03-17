nums = [5,9,1,1,2,10]
k = 9

def backtrack(index: int, total: int):
    if total == k:
        return 1
    elif total > k:
        return 0
    if index >= len(nums):
        return 0
    
    # pick
    pick = backtrack(index + 1, total + nums[index])
    
    # not pick
    not_pick = backtrack(index + 1, total)
    
    return pick + not_pick

count = backtrack(0, 0)
print(count)