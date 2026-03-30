coins = [1,2,5,10,20,50,100,200,500,2000]
N = 47
result = [] 
n = len(coins)
for i in range(n-1, -1, -1):
    while N >= coins[i]:
        N -= coins[i]
        result.append(coins[i])
print(result)