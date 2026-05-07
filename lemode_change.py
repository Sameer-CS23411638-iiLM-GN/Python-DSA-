bills = [5,5,5,10,20]
n = len(bills)
five = 0
ten = 0
for i in range(0,n):
    if bills[i] == 5:
        five += 1
    elif bills[i] == 10:
        if five > 0:
            five -= 1
            ten += 1
        else:
            print("False")
            break
    else:
        if ten > 0 and five > 0:
            ten -= 1
            five -= 1
        elif five >= 3:
            five -= 3
        else:
            print("False")
            break