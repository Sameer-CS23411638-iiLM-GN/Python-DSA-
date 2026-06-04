def minPlatforms_bruteforce(arr, dep):
    n = len(arr)
    max_platforms = 1

    for i in range(n):
        platforms = 1
        for j in range(n):
            if i != j:
                # check overlap
                if (arr[i] >= arr[j] and arr[i] <= dep[j]) or \
                   (arr[j] >= arr[i] and arr[j] <= dep[i]):
                    platforms += 1

        max_platforms = max(max_platforms, platforms)

    return max_platforms


# Example
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

print(minPlatforms_bruteforce(arr, dep))


#optimal (2 pointer approach)
def minPlatforms_optimal(arr, dep):
    n = len(arr)

    # Step 1: Sort both arrays
    arr.sort()
    dep.sort()

    i = 0  # arrival pointer
    j = 0  # departure pointer

    platforms = 0
    max_platforms = 0

    # Step 2: Traverse arrays
    while i < n and j < n:
        if arr[i] <= dep[j]:
            platforms += 1
            i += 1
        else:
            platforms -= 1
            j += 1

        max_platforms = max(max_platforms, platforms)

    return max_platforms


# Example
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

print(minPlatforms_optimal(arr, dep))