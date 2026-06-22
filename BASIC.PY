n = 5873
num = n 
while n >0:
    ld = n%10
    print(ld)
    n = n//10

n = 5873
num = n
while n >0:
    ld = n%10
    print(ld)
    n = n // 10

#count digits
n = 5483
num = n
count = 0
while n > 0:
    count += 1
    num = num//10
print(count)

n = 7865
num =n 
count = 0
while n > 0:
    count += 1
    n = n // 10
print(count)

#optimal approach
from math import *
def countDigits(num):
    return int(log10(num))+1

from math import *
def countDigits(num):
    return int(log10(num)+1)

#reverse a number
n = 5483
num = n
rev = 0
while n >0:
    rev = rev*10 + n%10
    n = n//10
print(rev)

n = 5483
num = n
rev = 0
while n > 0:
    rev = rev*10+n%10
    n = n//10
print(rev)

#check if a number is palindrome
n = 5483
num = n
result = 0
while n > 0:
    ld = num%10
    result = result*10 + ld
    num = num//10
print(n == result)

n = 5483
num = n
result = 0
while n > 0:
    ld = num%10
    result = result*10 + ld
    num = num//10
    print(n, result)
#Armstrong number
n = 153
num = n
total = 0
nod = len(str(n))
while n > 0:
    ld = n%10
    total += ld**nod
    n = n//10
print(total == num)

#print all factors of a number
result = []
for i in range(1, num+1):
    if num%i == 0:
        result.append(i)
print(result)

#optimal approach   
result = []
for i in range(1,num//2):
    if num%i == 0:
        result.append(i)
result.append(num)
print(result)

#optimal approach 2
from math import *
result = []
for i in range(1, int(sqrt(num))+1):
    if num%i == 0:
        result.append(i)
        if i != num//i:
            result.append(num//i)
print(result)


#brute force approach - check prime number
def isPrime(n):
    count = 0

    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    return count == 2

#optimal approach - check prime number
def isPrime(n):
    if n <= 1:
        return False
    
    for i in range(2,int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True
                       