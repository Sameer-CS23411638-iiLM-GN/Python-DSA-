#sliding window + pointer
s = "CADBZABCD"
n = len(s)
maxi = 0

for i in range(n):
    my_set = set()
    
    for j in range(i, n):
        if s[j] in my_set:
            break
        
        my_set.add(s[j])
        maxi = max(maxi, j - i + 1)

print(maxi)

#optimal
s = "CADBZABCD"
n = len(s)

my_dict = {}
left = 0
maxi = 0

for right in range(n):
    if s[right] in my_dict:
        left = max(left, my_dict[s[right]] + 1)
    
    my_dict[s[right]] = right
    maxi = max(maxi, right - left + 1)

