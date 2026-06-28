nums = [55,32,-97,98,3,67]
largest = nums[0]
n = len(nums)
for i in range(0,n):
    largest = max(largest,nums[i])
print(largest)


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

largest = float("-inf")
s_largest = float("-inf")
n = len(nums)
for i in range(0,n):
    largest=max(largest,nums[i])
for i in range(0,n):
    if nums[i]>s_largest and nums[i]!=largest:
        s_largest = nums[i]
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

nums = [3,5,8,6,1,0,2]
n = len(nums)
for i in range(0,n-1):
    if nums[i]>nums[i+1]:
        print(True)
print(False)

#Day - 2 
#remove the duplicate array
nums [1,1,1,2,3,4,4,7,9,9,9,10]
n = len(nums)
freq_map = {}
for i in range(0,n):
    freq_map[nums[i]] = 0
j = 0
for k in freq_map:
    nums[j] = k
    j += 1
print (j)

n = len(nums)
freq_map = {}
for i in range(0,n):
    freq_map[nums[i]] = 0
j = 0
for k in freq_map:
    nums[j] = k
    j += 1
print(j)

#optimal solution
n = len(nums)
if n == 1:
    print(1)
i = 0
j = i+1
while j<n:
    if nums[j]!=nums[i]:
        i+=1
        nums[i],nums[j] = nums[j],nums[i]
    j+=1
print(i+1)

n = len(nums)
if n == 1:
    print(1)
i = 0
j = i+1
while j<n:
    if nums[j]!=nums[i]:
        i+= 1
        nums[i],nums[j] = nums[j],nums[i]
    j += 1
print(i+1)

#rotate array by 1 place
nums = [5,-2,3,9,0,6,10,7]
n = len(nums)

nums[:] = [nums[-1]] + nums[0:n-1]

print(nums)

#same but another method
temp = nums[n-1]
for i in range(n-2,-1,-1):
    nums[i+1] = nums[i]
nums[0] = temp 

#rotate the array by k places
#brute force approach
nums=[3,9,5,6,7,2]
for _ in range(0,k):
    e = nums.pop()
    nums.insert(0,e)
print(nums)

#anotherr brute force
n = len(nums)
rotations = k%n
for _ in range(0,k):
    e = nums.pop()
    nums.insert(0,e)
print(nums)

#through slicing optimal 
nums=[3,9,5,6,7,2]
n = len(nums)
k = n%k
nums[:] = nums[n-k:]+nums[:n-k]

#without slicing
nums=[3,9,5,6,7,2]
def reverse(nums,left,right):
    while left<right:
        nums[left]+nums[right] = nums[right]+nums[left]
        left+=1
        right-=1
reverse(n-k,n-1) #reverse last K element
reverse(0,n-k-1) #reverse remainig element
reverse(0,n-1) #reverse whole array

#move zeros to end
# brute force
nums = [1,0,2,4,3,0,0,3,5,1]

count = nums.count(0)

for _ in range(count):
    nums.remove(0)    # removes the first occurrence of 0
    nums.append(0)

print(nums)

#brute force 2
nums = [1,0,2,4,3,0,0,3,5,1]
n = len(nums)
temp = []
for i in range(0,n):
    if nums[i]!=0:
        temp.append(nums[i])
nz = len(temp)
for i in range(0,nz):
    nums[i] = temp[i]
for i in range(nz,n):
    nums[i] = 0

#optimal solution in single pass
nums = [1,0,2,4,3,0,0,3,5,1]
if len(nums) == 1:
    print
i = 0
while i<len(nums):
    if nums[i] == 0:
        break
    i+=1
if i==len(nums):
    print
j = i+1
while j<len(nums):
    if nums[j]!=0:
        nums[i],nums[j] = nums[j],nums[i]
        i+=1
    j+=1

#linear search
nums = [5,3,9,8,1,6,4,-10,-100]
target = 4
n = len(nums)
for i in range(0,n):
    if nums[i] == target:
        print(i)
print("-1")

#merge 2 sorted list , remove duplicataes and sort them
nums1 = [1,1,1,1]
nums2 = [2,2,2,2]
#brute force
# Merge
nums = nums1 + nums2

# Remove duplicates
nums = list(set(nums))

# Sort
nums.sort()

print(nums)

#optimal using  pointers
def union(nums1, nums2):
    n = len(nums1)
    m = len(nums2)

    result = []
    i = 0
    j = 0

    while i < n and j < m:
        if nums1[i] <= nums2[j]:
            if len(result) == 0 or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1
        else:
            if len(result) == 0 or result[-1] != nums2[j]:
                result.append(nums2[j])
            j += 1

    while i < n:
        if len(result) == 0 or result[-1] != nums1[i]:
            result.append(nums1[i])
        i += 1

    while j < m:
        if len(result) == 0 or result[-1] != nums2[j]:
            result.append(nums2[j])
        j += 1

    return result


nums1 = [1, 1, 1, 2, 4, 6, 7]
nums2 = [1, 2, 3, 6, 7, 8, 9, 10]

print(union(nums1, nums2))

#find the missing number
nums = [9,6,4,2,3,5,7,0,1]
n = len(nums)
for i in range(0,n+1):
    if i not in nums:
        print(i)

#optimal
n = len(nums)
freq = {}
for i in range(0,n+1):
    freq[i] = 0
for num in nums:
    freq[num] = 1
for k,u in freq.items():
    if u==0:
        print(k)
#more optimal
nums = [9,6,4,2,3,5,7,0,1]
n = len(num)
print (n * (n + 1) // 2) - sum(nums)

#max consecutive one

nums = [1,0,0,0,1,1,1,1,1,0,0,0,1,1,0]
n = len(nums)
count = float("-inf")
largest = float("-inf")
for i in range(0,n):
    if nums[i] == 1:
        count += 1
    else:
        count = 0
    
    largest = max(count,largest)
print(largest)

#2 sum problem

nums[1,3,5,9,1,3,1,4]
target = 10

  # n = len(nums)
        # for i in range(0,n-1):
        #     for j in range(i+1,n):
        #         if nums[i]+nums[j] == target:
        #             return(i,j)
n = len(nums)
hash_map = {}
for i in range(0,n):
    remaining = target - nums[i]
    if remaining in hash_map:
        print[hash_map[remaining],i]
    hash_map[nums[i]] = i
