def searchBST(root, value):
    temp = root
    while temp is not None:
        if temp.value == value:
            return temp
        elif temp.value < value:
            temp = temp.right
        else:
            temp = temp.left
    return None