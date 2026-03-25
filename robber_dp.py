from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = 0  # best till previous house
        prev2 = 0  # best till house before that
        
        for num in nums:
            take = prev2 + num   # rob this house
            skip = prev1         # skip this house
            
            curr = max(take, skip)
            
            # update values
            prev2 = prev1
            prev1 = curr
        
        return prev1