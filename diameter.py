diameter = 0

def solve(node):
    global diameter
    
    if node is None:
        return 0
    
    left_height = solve(node.left)
    right_height = solve(node.right)
    
    # Update diameter
    diameter = max(diameter, left_height + right_height)
    
    # Return height
    return max(left_height, right_height) + 1


def diameter_of_tree(root):
    global diameter
    diameter = 0
    solve(root)
    return diameter