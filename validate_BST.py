def isValidBST(root):
    def solve(node, low, high):
        if not node:
            return True

        # Check current node value against bounds
        if not (low < node.val < high):
            return False

        # Left subtree → values must be < node.val
        if not solve(node.left, low, node.val):
            return False

        # Right subtree → values must be > node.val
        return solve(node.right, node.val, high)

    return solve(root, float('-inf'), float('inf'))


"""class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        curr = root

        while True:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p == curr:
                return p
            elif q == curr:
                return q
            else:
                return curr"""