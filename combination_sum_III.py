# def solve(last,total,subset):
#     if total==n and len(subset) == K:
#         result.append(subset.copy())
#         return
#     if total>n or len(subset)>k:
#         return
#     for i in range(last,10):
#         sum = total+i
#         susbet.append(i)
#         Solve(i+1,sum,subset)
#         subset.pop()
#     solve[1,0,[]]


def solve(last, total, subset):
    if total == n and len(subset) == k:
        result.append(subset.copy())
        return
    
    if total > n or len(subset) > k:
        return
    
    for i in range(last, 10):
        subset.append(i)
        solve(i + 1, total + i, subset)
        subset.pop()


# ---- Example Run ----
n = 7   # target sum
k = 3   # size of subset
result = []

solve(1, 0, [])

print(result)