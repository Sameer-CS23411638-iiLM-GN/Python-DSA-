nums = [55,32,-97,98,3,67]
largest = nums[0]
n = len(nums)
for i in range(0,n):
    largest = max(largest,nums[i])
print(largest)

#method 2
largest = float("-inf")
n = len(nums)
for i in range(0,n):
    largest = max(largest,nums[i])
print(largest)

#2nd largest element
#brute force - sort the given array..it will get sorted into the ascending order then return the last second index(n-2) value
#better
nums = [55,32,97,-55,45,32,88,21]
largest = float("-inf")
s_largest = float("-inf")
n = len(nums)
for i in range(0,n):
    largest = max(largest,nums[i])
for i in range(0,n):
    if nums[i]>s_largest and nums[i]!=largest:
        s_largest = nums[i]
print(s_largest)

#optimal solution
largest = float("-inf")
s_largest = float("-inf")
for i in range(0,n):
    if nums[i]>largest:
        s_largest = largest
        largest = nums[i]
    elif nums[i]>s_largest and nums[i]!=largest:
        s_largest = nums[i]
print(s_largest)

#check if array is sorted or not return True or false
nums = [3,5,10,12,16,18]
n = len(nums)
for i in range(0,n-1):
    if nums[i]>nums[i+1]:
        print("False")
print("True")