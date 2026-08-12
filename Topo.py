class Solution:
    def dfs(self,current_node,visited,stack,adj_list):
        visited[current_node]  = 1
        for adjNode in adj_list[current_node]:
            if visited[adjNode] == 0:
                self.dfs(adjNode,visited,stack,adj_list)
        stack.append(current_node)
    def topoSort(self, V, adj_list):
        visited = [0]*V
        stack = []
        for i in range(V):
            if visited[i] == 0:
                self.dfs(i,visited,stack,adj_list)
        return stack[::-1]