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