# nums = [1,2,3]
# #brute force approach
# n = len(nums)
# total_subsets = 1 << n
# result = []
# for num in range(0,total_subsets):
#     1st = []
#     for i in range(0,n):
#         if num & (1 << i)!=0:
#             1st.append(nums[i])
#     result.append(1st)
# print(result)