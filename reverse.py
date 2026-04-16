n = int(input("enter the number: "))
num = n
reverse = 0
while n>0:
    rem = n %10
    reverse = reverse *10 +rem
    n = n // 10
print(reverse)

# n = int(input("enter the number: "))
# num = n
# reverse = 0
# while n>0:
#     rem = n %10
#     reverse = reverse *10 +rem
#     n = n // 10