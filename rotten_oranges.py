from collections import deque
from copy import deepcopy
from typing import List

def orangesRotting(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    grid_copy = deepcopy(grid)

    fresh_cnt = 0
    queue = deque()

    # Initialize queue and count fresh oranges
    for r in range(rows):
        for c in range(cols):
            if grid_copy[r][c] == 2:
                queue.append((r, c))
            elif grid_copy[r][c] == 1:
                fresh_cnt += 1

    minutes = 0

    # BFS
    while len(queue) != 0 and fresh_cnt > 0:
        minutes += 1
        total_rotten = len(queue)

        for _ in range(total_rotten):
            i, j = queue.popleft()

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_i = i + dx
                new_j = j + dy

                # Boundary check
                if new_i < 0 or new_i == rows or new_j < 0 or new_j == cols:
                    continue

                # Skip empty or already rotten
                if grid_copy[new_i][new_j] == 0 or grid_copy[new_i][new_j] == 2:
                    continue

                # Rot the fresh orange
                fresh_cnt -= 1
                grid_copy[new_i][new_j] = 2
                queue.append((new_i, new_j))

    if fresh_cnt > 0:
        return -1

    return minutes

grid = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]
print(orangesRotting(grid))