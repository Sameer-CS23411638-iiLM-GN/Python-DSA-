#find the maximum number 
nums = [55,32,-97,98,3,67]
n = len(nums)
largest = float("-inf")
for i in range(0,n):
    largest = max(nums[i],largest)
print(largest)

#find the second maximum number
nums = [55,32,-97,98,3,67]
largest = float("-inf")
s_largest = float("-inf")
n = len(nums)
for i in range(0,n):
    largest = max(nums[i],largest)
for i in range(0,n):
    if nums[i]>s_largest and nums[i]!=largest:
        s_largest = nums[i]
print(s_largest)

#check if array is sorted
nums = [55,32,-97,98,3,67]
n = len(nums)
for i in range(0,n-1):
    if nums[i]>nums[i+1]:
        print("false")
print("true")

#remove the duplicate

nums = [1,1,1,2,3,4,4,7,9,9,9,10]
n = len(nums)
freq_map = {}
for i in range(0,n):
    freq_map[nums[i]] = 0
j = 0
for k in freq_map:
    nums[j]=k
    j += 1
print(j)

#rotate the array by 1 place

nums=[3,9,5,6,7,2]
nums[:] = nums[-1:]+nums[0:5]
print(nums)

#rotate the array by k places

nums = [3,9,5,6,7,2]
k = int(input("enter the value of k"))
n = len(nums)
l = n%k
nums[:] = nums[n-k:] + nums[:n-k]
print(nums)
