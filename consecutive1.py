def countBinaryStrings(n):
    if n == 1:
        return 2  # 0, 1
    
    a = 1  # ending with 0
    b = 1  # ending with 1
    
    for i in range(2, n+1):
        new_a = a + b
        new_b = a
        
        a = new_a
        b = new_b
    
    return a + b

#recursion


def countBinaryStrings(n, prev):
    # base case
    if n == 0:
        return 1
    
    # always allowed to place 0
    count = countBinaryStrings(n-1, 0)
    
    # place 1 only if previous was not 1
    if prev == 0:
        count += countBinaryStrings(n-1, 1)
    
    return count

# call
print(countBinaryStrings(3, 0))