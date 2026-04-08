def kthSmallest(root, k):
    count = 0
    result = None

    def inorder(node):
        nonlocal count, result
        if not node or result is not None:
            return
        
        inorder(node.left)
        
        count += 1
        if count == k:
            result = node.value
            return
        
        inorder(node.right)

    inorder(root)
    return result