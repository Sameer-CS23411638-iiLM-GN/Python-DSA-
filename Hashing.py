# from pyparsing import nums


# freq_map = dict()/{}
# for i in range(len(nums)):
#     if nums[i] in freq_map:
#         freq_map[nums[i]] += 1
#     else:
#         freq_map[nums[i]] = 1
# print(freq_map[nums[0]])

# #optimal 2

# nums = [1,2,3,4,5,6,7,8,9]
# hash_map = dict()/{}
# n = len(nums)
# for i in range(0,n):
# hash_map[nums[i]] = hash_map.get(nums[i],0) + 1
# print(hash_map[nums[0]])


n = [1,2,3,4,5,6,7,8,9]
m = [1,2,3,4,5,6,7,8,9]
hash_map = dict()/{}
for num in m:
    count = 0
    for x in num:
        if x == num:
            count += 1
            print(count)

n = [ 1,2,3,4,5,6,7,8,9 ]
m = [ 1,2,3,4,5,6,7,8 ]
hash_map = dict()/{}
for num in m:
    count = 0
    for x in n:
        if x == num:
            count += 1
            print(count)


#optimal 2
n = [1,2,3,4,5,6,7,8,9]
m = [1,2,3,4,5,6,7,8]
hash_list = dict()/{}
hash_list=[0]*11
for num in n:
    hash_list[num] += 1
for num in m:
    if num<1 or num>10:
        print(0)
    else:
        print(hash_list[num])

n = [1,2,3,4,5,6,7,8,9]
m = [1,2,3,4,5,6,7,8]
hash_list = [0]*11
for num in n:
    hash_list[num] += 1
    for num in m:
        if num < 1 or num > 10:
            print(0)
        else:
            print(hash_list[num])

#Character Hashing
s = "abcde"
q = ["a", "b", "c", "d", "e", "f"]
for ch in s:
    ascii_value = ord(ch)
    index = ascii-97
    hash_list[index] += 1
    
for ch in q:
    ascii_val=ord(ch)
    index=ascii_val-97
    print(hash_list[index])

#character hashing optimal 2

s = "abcde"
q = ["a", "b", "c", "d", "e", "f"]
for ch in s:
    ascii_value = ord(ch)
    index = ascii_value - 97
    hash_list[index] += 1

for ch in q:
    ascii_val = ord(ch)
    index = ascii_val - 97
    print(hash_list[index])

s = "abcde"
q = ["a", "b", "c", "d", "e", "f"]
for ch in s:
    ascii_value = ord(ch)
    index = ascii_value - 97
    hash_list[index] += 1

for ch in q:
    ascii_val = ord(ch)
    index = ascii_val - 97
    hash_list[index] += 1
    print(hash_list[index])