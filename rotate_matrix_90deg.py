# Example Matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

n = len(matrix)
result = [[0 for _ in range(n)]  for _ in range(n)]
for i in range(n):
    for j in range(n):
        result[j][(n - 1) - i] = matrix[i][j]
print(result)

#optimal
n = len(matrix)
for i in range(n):
    for j in range(i, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
for i in range(n):
    matrix[i].reverse()