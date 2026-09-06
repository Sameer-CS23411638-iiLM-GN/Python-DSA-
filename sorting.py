#selection sort
nums = [5, 2, 9, 1, 5, 6]
def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        mini_index = i
        for j in range(i+1, n ):
            if nums[j] < nums[mini_index]:
                mini_index = j
        nums[i],nums[mini_index] = nums[mini_index], nums[i]
print("Before sorting:", nums)

#bubble sort(adjacent swapping)
nums = [5, 2, 9, 1, 5, 6]
n = len(nums)
for i in range(n-2, -1, -1):
    is_swap = False
    for j in range(i+1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1] = nums[j+1], nums[j]
            is_swap = True
    if is_swap == False:
        break

#Insertion sort
nums = [5, 2, 9, 1, 5, 6]
n = len(nums)
for i in range(1,n):
    key = nums[i]
    j = i-1
    while j>=0 and nums[j]>key:
        nums[j+1] = nums[j]
        j -= 1
        nums[j+1] = key

#Merge sort
arr = [4,5,3,3,6,7,8,9,10]
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr) // 2
    left_arr = nums[:mid]
    right_arr = nums[mid:]
    left = merge_sort[left_arr]
    right = merge_sort[right_arr]
#print merge_sort(left,right)
