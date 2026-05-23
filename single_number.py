arr = [5,1,3,3,7,1,7]
#output = 5
#brute force approach
hash_map = {}
for num in arr:
    hash_map[num] = hash_map.get(num,0)+1
for key in hash_map:
    if hash_map[key] == 1:
        print(key)

#optimal(bit manipulation)
ans = 0
for num in arr:
    ans = ans ^ num
print(ans)
