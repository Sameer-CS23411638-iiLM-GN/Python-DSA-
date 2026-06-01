from typing import List

class Solution:
    def solve(self, index, total, subset, nums, target, result):
        if total == target:
            result.append(subset.copy())
            return
        elif total > target:
            return
        
        if index >= len(nums):
            return
        
        # Include current element
        total += nums[index]
        subset.append(nums[index])
        self.solve(index, total, subset, nums, target, result)
        
        # Backtrack
        total -= nums[index]
        subset.pop()
        
        # Exclude current element
        self.solve(index + 1, total, subset, nums, target, result)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.solve(0, 0, [], candidates, target, result)
        return result


# ---- Example Run ----
sol = Solution()
candidates = [2, 3, 6, 7]
target = 7

output = sol.combinationSum(candidates, target)
print(output)