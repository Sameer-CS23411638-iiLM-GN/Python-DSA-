def searchBST(root, value):
    inp = 13
    ceil = -1
    while root is not None:
        if root.value == inp:
            return root.key
        elif root.key<inp:
            root = root.right
        else:
            ceil = root.key
            root = root.left
    return ceil