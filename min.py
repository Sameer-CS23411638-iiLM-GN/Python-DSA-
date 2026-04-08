def searchBST(root, value):
    while root is not None and root.left is not None:
        root = root.left
    return root.datassssssss