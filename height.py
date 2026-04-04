from collections import deque

def level_order(root):
    if root is None:
        return 0

    queue = deque([root])
    height = 0

    while len(queue) != 0:
        level_size = len(queue)   # number of nodes at current level
        height += 1

        for _ in range(level_size):
            node = queue.popleft()

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

    return height