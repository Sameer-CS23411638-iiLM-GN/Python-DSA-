from collections import deque

def bfs(start, graph):
    visited = [False] * len(graph)   # assuming nodes are 0 to n-1
    result = []

    q = deque()
    
    # Step 1: initialize
    q.append(start)
    visited[start] = True

    # Step 2: BFS traversal
    while q:
        node = q.popleft()
        result.append(node)

        # Step 3: explore neighbors
        for neighbor in graph[node]:
            if not visited[neighbor]:
                q.append(neighbor)
                visited[neighbor] = True

    return result

graph = [
    [1, 2],    # 0
    [0, 3, 4], # 1
    [0, 5],    # 2
    [1],       # 3
    [1, 5],    # 4
    [2, 4]     # 5
]

print(bfs(0, graph))