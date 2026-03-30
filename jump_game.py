def can_jump(nums):
    max_index = 0

    for i in range(len(nums)):
        # If current index is not reachable
        if i > max_index:
            return False
        
        # Update the farthest reachable index
        max_index = max(max_index, i + nums[i])

    return True


# 🔹 Example Usage
nums = [3, 2, 1, 0, 0, 2, 1, 5]
print(can_jump(nums))   # Output: False