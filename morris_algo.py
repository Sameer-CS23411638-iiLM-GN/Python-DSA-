from typing import List, Optional

# Definition of TreeNode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Inorder Traversal (Morris Traversal)
def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    result = []
    current = root

    while current is not None:
        if current.left is None:
            result.append(current.val)
            current = current.right
        else:
            predecessor = current.left

            # Find the rightmost node in left subtree
            while predecessor.right is not None and predecessor.right != current:
                predecessor = predecessor.right

            # Create thread
            if predecessor.right is None:
                predecessor.right = current
                current = current.left
            else:
                # Remove thread
                predecessor.right = None
                result.append(current.val)
                current = current.right

    return result