def findSuccessor(root, key):
    successor = None
    curr = root

    while curr:
        if curr.data > key:
            successor = curr
            curr = curr.left
        else:
            curr = curr.right

    return successor


def findPredecessor(root, key):
    predecessor = None
    curr = root

    while curr:
        if curr.data < key:
            predecessor = curr
            curr = curr.right
        else:
            curr = curr.left

    return predecessor