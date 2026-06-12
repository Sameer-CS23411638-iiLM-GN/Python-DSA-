def lowerBound(nums, target):
    n = len(nums)
    lb = -1
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1

    return lb


def upperBound(nums, target):
    n = len(nums)
    ub = n
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1

    return ub


def countOccurrences(nums, target):
    lb = lowerBound(nums, target)

    # If target not found
    if lb == -1 or nums[lb] != target:
        return 0

    ub = upperBound(nums, target)

    return ub - lb


# 🔹 Taking array by myself (Sorted Array Required)
nums = [1, 2, 2, 2, 3, 4, 5, 5, 6]
target = 2

print("Count of", target, "=", countOccurrences(nums, target))