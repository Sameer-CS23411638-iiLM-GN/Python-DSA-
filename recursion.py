#Head recursion
from ast import arg


def func():
    if count == 4:
        return
    print("Sameer")
    count += 1
    func()
func()

#Tail recursion
count = 0
def func():
    if count == 4:
        return
    count += 1
    func()
    print("Sameer")

def func(x,n):
    if n==0:
        return
    print(x)
    func(x,n-1)
    
def func(i,N):
    if i > N:
        return
    print(i)
    func(i+1,N)

def factorial (num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num-1)

#nums.reverse() inbuilt function
# nums[::-1]
# def func(nums,left,right):
#     if left>=right:
#         return
#     arg[left],arg[right] = arg[right],arg[left]
#     func(arg,left+1,right-1)
# def reverseArray(nums,l,r):
#     self.funs(nums,l,r)
#     return nums

#2 pointers approach
S = "ANBDDJAFSKH"
n = len(S)
left = 0
right = n-1
while left < right:
    if S[left] != S[right]:
        print(False)
    left += 1
    right -= 1
print(True)

def func(S,left,right):
    if left>= right:
        return True
    if S[left] != S[right]:
        return False
    return func(S,left+1,right-1)