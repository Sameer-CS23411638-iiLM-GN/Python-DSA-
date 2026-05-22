nums = [ -1 , 0 , 1 , 2 , -1 , -4 ]
n = len(nums)
my_set = set()
target = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            for l in range(k+1, n):
                if nums[i] + nums[j] + nums[k] + nums[l] == target:
                    my_set.add(tuple(sorted((nums[i], nums[j], nums[k], nums[l]))))
print([list(ans) for ans in my_set])

#optimal solution
nums.sort()
n = len(nums)
my_set = set()
target = 0
for i in range(n):
    for j in range(i+1, n):
        left = j + 1
        right = n - 1
        while left < right:
            sum_ = nums[i] + nums[j] + nums[left] + nums[right]
            if sum_ == target:
                my_set.add((nums[i], nums[j], nums[left], nums[right]))
                left += 1
                right -= 1
            elif sum_ < target:
                left += 1
            else:
                right -= 1