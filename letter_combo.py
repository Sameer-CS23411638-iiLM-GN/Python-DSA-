def solve(index, subset):
    if index >= len(nums):
        result.append(subset.copy())
        return
    
    # Include element
    subset.append(nums[index])
    solve(index + 1, subset)
    
    # Backtrack
    subset.pop()
    
    # Exclude element
    solve(index + 1, subset)


# ---- Example Run ----
nums = [1, 2, 3]
result = []

solve(0, [])

print(result)