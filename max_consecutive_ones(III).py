#brute 
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
maxi=0
n = len(nums)
for i in range(0,n):
    zeros = 0
    for j in range(i,n):
        if nums[j]==0:
            zeros += 1
            if zeros>k:
                break
            maxi = max(maxi,j-i+1)
print(maxi) 
#better 
def longestOnes(nums, k):
    left = 0
    zeros = 0
    maxi = 0

    for right in range(len(nums)):
        # If we see a zero, increase count
        if nums[right] == 0:
            zeros += 1

        # If zeros exceed k, shrink window
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        # Update max length
        maxi = max(maxi, right - left + 1)

    return maxi


# Example input
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2

# Output
print("Maximum consecutive 1s:", longestOnes(nums, k))


# #optimal
def longestOnes(nums, k):
    left = 0
    zeros = 0
    maxi = 0

    for right in range(len(nums)):
        # If we see a zero, increase count
        if nums[right] == 0:
            zeros += 1

        # If zeros exceed k, shrink window
        if zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        # Update max length
        maxi = max(maxi, right - left + 1)

    return maxi


# Example input
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2

# Output
print("Maximum consecutive 1s:", longestOnes(nums, k))