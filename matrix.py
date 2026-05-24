from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        distance = [[0 for _ in range(cols)] for _ in range(rows)]
        
        queue = deque()
        
        # Step 1: Push all 0s into queue
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c, 0))
                    visited[r][c] = 1
        
        # Directions (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Step 2: BFS
        while queue:
            i, j, d = queue.popleft()
            distance[i][j] = d

            for dr, dc in directions:
                ni, nj = i + dr, j + dc

                if 0 <= ni < rows and 0 <= nj < cols and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    queue.append((ni, nj, d + 1))

        return distance
    
mat = [
    [0,0,0],
    [0,1,0],
    [1,1,1]
]

sol = Solution()
print(sol.updateMatrix(mat))
    