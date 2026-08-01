def totalFruit(nums):
    left = 0
    right = 0
    max_length = 0
    my_dict = {}

    n = len(nums)

    while right < n:
        # Add current fruit
        my_dict[nums[right]] = my_dict.get(nums[right], 0) + 1

        # If more than 2 types → shrink window
        while len(my_dict) > 2:
            my_dict[nums[left]] -= 1

            if my_dict[nums[left]] == 0:
                del my_dict[nums[left]]

            left += 1

        # Update max length
        max_length = max(max_length, right - left + 1)

        right += 1

    return max_length


# Example from image
nums = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]

print("Maximum fruits:", totalFruit(nums))