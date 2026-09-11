nums = [5,9,1,2,4,15,6,3]
target = 10

#brute force approach
# n = len(nums)
# for i in range(0,n-1):
#     for j in range(i+1,n):
#         if nums[i]+nums[j] == target:
#             print(i,j)

#optimal approach
n = len(nums)
hash_map = {}

for i in range(n):
    remaining = target - nums[i]
    
    if remaining in hash_map:
        print([hash_map[remaining], i])
        break   # stop after finding pair
    
    hash_map[nums[i]] = i

# n - len(nums)
# hash_map = {}
# for i in range(0,n):
#     remaining = target - nums[i]

#     if remaining in hash_map:
#         print([hash_map[remaining],i])
#         break

#     hash_map[nums[i]] - i


    