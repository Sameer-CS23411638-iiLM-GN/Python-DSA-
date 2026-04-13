#DFS approach
from typing import List

def floodFillDFS(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    rows, cols = len(image), len(image[0])
    original = image[sr][sc]

    # Edge case: same color
    if original == newColor:
        return image

    def dfs(r, c):
        # boundary + color check
        if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original:
            return

        image[r][c] = newColor

        # 4 directions
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    dfs(sr, sc)
    return image

#BFS approach
from collections import deque
from typing import List

def floodFillBFS(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    rows, cols = len(image), len(image[0])
    original = image[sr][sc]

    if original == newColor:
        return image

    q = deque()
    q.append((sr, sc))
    image[sr][sc] = newColor

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while q:
        r, c = q.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original:
                image[nr][nc] = newColor
                q.append((nr, nc))

    return image