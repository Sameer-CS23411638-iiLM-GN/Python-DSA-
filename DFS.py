#DFS FOR DISCONNECTED GRAPH

def dfs_all(graph):
    visited = [False] * len(graph)
    result = []

    def dfs(node):
        visited[node] = True
        result.append(node)

        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)

    for i in range(len(graph)):
        if not visited[i]:
            dfs(i)

    return result

#iterative DFS for stack version 

def dfs_iterative(start, graph):
    visited = [False] * len(graph)
    stack = [start]
    result = []

    while stack:
        node = stack.pop()

        if not visited[node]:
            visited[node] = True
            result.append(node)

            # push neighbors (reverse for same order as recursion)
            for neighbor in reversed(graph[node]):
                if not visited[neighbor]:
                    stack.append(neighbor)

    return result