maxi = float('-inf')
def Solve(node):
    if node is None:
        return 0
    left_sum = Solve(node.left)
    if left_sum<0:
        left_sum = 0
    right_sum = Solve(node.right)
    if right_sum<0:
        right_sum = 0
    maxi = max(maxi, left_sum + right_sum + node.value)
    return max(left_sum, right_sum) + node.value