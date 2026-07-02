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


#max consecutive one
nums = [1,0,0,0,1,1,1,1,1,0,0,0,1,1,0]
n = len(nums)
largest = float("-inf")
count = 0
for i in range(0,n):
    if nums[i] == 1:
        count += 1
    else: 
        count = 0
    largest = max(largest,count)
print(largest)


#2 sum problem

nums=[1,3,5,9,1,3,1,4]
target = 10

n = len(nums)
hash_map={}
for i in range(0,n):
    remaining = target - nums[i]
    if remaining in hash_map:
        print([hash_map[remaining],i])
        hash_map[nums[i]] = i


#print max sub array
nums = [-2,1,-3,4,-1,2,1,-5,4]
n = len(nums)
total = 0
maxi = float("-inf")
for i in range(0,n):
    total = total + nums[i]
    maxi = max(maxi,total)
    if total < 0:
        total = 0
print(maxi)


#buy and sell stock
prices = [7,2,1,5,6,4,8]
n = len(prices)
max_profit = 0
min_prices= float("inf")
for i in range(0,n):
    min_price =  min(min_prices,prices[i])
    max_profit = max(max_profit,prices[i]-min_prices)
print(max_profit)

#arrange the element by their sign
nums = [5,10,-3,-1,-10,6]
n = len(nums)
result = [0]*n
pos , neg = 0 , 1
for i in range(0,n):
    if nums[i]>0:
        result[pos] = nums[i]
        pos += 2
    else:
        result[neg] = nums[i]
        neg += 2
print(result)


