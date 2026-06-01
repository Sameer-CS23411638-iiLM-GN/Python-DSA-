# def backtrack(index,total,subset):
#     if total == 0:
#         result.append(subset.copy())
#         return
#     if total<0:
#         return
#     if index>=len(nums):
#         return
#     for i in range(index,n):
#         if i>index and nums[i]==nums[i-1]:
#             continue
#         subset.append(nums[i])
#         sum=total-nums[i]
#         backtrack(i+1,sum,subset)
#         subset.pop()
from typing import List

def combinationSum2(nums: List[int], target: int) -> List[List[int]]:
    def backtrack(index, total, subset):
        if total == 0:
            result.append(subset.copy())
            return
        if total < 0:
            return
        
        for i in range(index, len(nums)):
            # Skip duplicates
            if i > index and nums[i] == nums[i - 1]:
                continue
            
            subset.append(nums[i])
            backtrack(i + 1, total - nums[i], subset)
            subset.pop()
    
    nums.sort()  # Important for handling duplicates
    result = []
    backtrack(0, target, [])
    return result


# ---- Example Run ----
nums = [10, 1, 2, 7, 6, 1, 5]
target = 8

output = combinationSum2(nums, target)
print(output)