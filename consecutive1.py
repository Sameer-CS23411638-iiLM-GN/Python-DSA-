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