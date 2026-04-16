# by using recursion
nums = [5,7,3,2,6,1,5,4]
def func(nums,left,right):
    if left>=right:
        return
    nums[left],nums[right] = nums[right],nums[left]
    func(nums,left+1,right-1)
def reverse_array(nums,l,r):
    func(nums,l,r)
    return nums

# def func(nums,left,right):
#     if left>=right:
#         return 
#     nums[left],nums[right] = nums[right],nums[left]
#     func(nums,left+1,right-1)
# def reverse_array(nums,l,r):
#     func(nums,l,r)
#     return nums

# nums = [5,7,3,2,6,1,5,4]
# def func(nums,left,right):
#     if left>=right:
#         return
#     nums[left],nums[right] = nums[right],nums[left]
#     func(nums,left+1,right-1)
# def reverse_array(nums,l,r):
#     func(nums,l,r)
#     return nums
#by using while loop

# nums = [5,7,3,2,6,1,5,4]

# def reverse_array(nums):
#     left = 0
#     right = len(nums) - 1
    
#     while left < right:
#         nums[left], nums[right] = nums[right], nums[left]
#         left += 1
#         right -= 1
        
#     return nums

# print(reverse_array(nums))


# nums = [5,7,3,2,6,1,5,4]    
# def reverse_array(nums):
#     left = 0
#     right = len(nums) - 1
    
#     while left < right:
#         nums[left], nums[right] = nums[right], nums[left]
#         left += 1
#         right -= 1
        
#     return nums