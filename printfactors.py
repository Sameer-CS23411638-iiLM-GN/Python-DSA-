# num = 20
# result = []
# for i in range(1,num+1):
#     if num%i == 0:
#         result.append(i)
# print(result)

# num = 20
# result = []
# for i in range(1,num+1):
#     if num%i == 0:
#         result.append(i)
# print(result)

#Method 2
# n = int(input("enter the number: "))
# result = []
# for i in range(1,n//2):
#     if n%i == 0:
#         result.append(i)    
# result.append(n)
# print(result)

# n = int(input("enter the number: "))
# result = []
# for i in range(1,n//2):
#     if n%i == 0:
#         result.append(i)
# result.append(n)
# print(result)

#Method 3
from math import *
n = int(input("enter the number: "))
result = []
for i in range(1,int(sqrt(n))+1):
    if n%i == 0:
        result.append(i)
        if i != n//i:
            result.append(n//i)
result.sort()
print(result)

from math import *
n = int(input("enter the number: "))
result = []
for i in range(1,int(sqrt(n))+1):
    if n%i == 0:
        result.append(i)
        if i != n//i:
            result.append(n//i)

# from math import *
# n = int(input("enter the number: "))
# result = []
# for i in range(1,int(sqrt(n))+1):
#     if n%i == 0:
#         result.append(i)
#         if i != n//i:
#             result.append(n//i)
# result.sort()
# print(result)