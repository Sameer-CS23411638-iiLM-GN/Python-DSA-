from collections import deque

def isCycle(V, adj):
    visited = [0] * V
    
    for i in range(V):
        if visited[i] == 0:
            # BFS traversal
            q = deque([(i, -1)])
            visited[i] = 1
            
            while q:
                node, parent = q.popleft()
                
                for adj_node in adj[node]:
                    if visited[adj_node] == 0:
                        visited[adj_node] = 1
                        q.append((adj_node, node))
                    
                    elif adj_node != parent:
                        # Cycle detected
                        return True
    return False