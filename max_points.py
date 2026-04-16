def maxScore(nums, k):
    n = len(nums)

    # If taking all cards
    if k == n:
        return sum(nums)

    # Step 1: take first k elements (all from left)
    left_sum = sum(nums[:k])
    max_sum = left_sum

    right_sum = 0
    right_index = n - 1

    # Step 2: shift window (take from right, remove from left)
    for i in range(k - 1, -1, -1):
        left_sum -= nums[i]                 # remove from left
        right_sum += nums[right_index]      # add from right

        max_sum = max(max_sum, left_sum + right_sum)

        right_index -= 1

    return max_sum


# Example from image
nums = [1, 2, 3, 4, 5, 6, 1]
k = 3

print("Maximum score:", maxScore(nums, k))