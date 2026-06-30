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

##move zeros to end
# brute force
nums = [1,0,2,4,3,0,0,3,5,1]
n = len(nums)
for i in range(0,n):
    nums.remove(0)
    nums.append(0)
print(nums)

#linear search

nums = [5,3,9,8,1,6,4,-10,-100]
target = 4
n = len(nums)
for i in range(0,n):
    if nums[i]==target:
        print(i)
print("-1")


#merge 2 sorted list , remove duplicataes and sort them
nums1 = [1,1,3,1,4,5,6]
nums2 = [2,2,2,2,100,15]
n = nums1+nums2
n = list(set(n))
n.sort()
print(n)

#find the missing number
nums = [9,6,4,2,3,5,7,0,1]
n = len(nums)
print(n*(n+1)//2 - sum(nums))

