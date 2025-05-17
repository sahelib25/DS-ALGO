class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Create an adjacency list
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u) # Since the graph is undirected

        visited = [False] * n

        def dfs(node):
            
            if node == destination:
                return True
            visited[node] = True
            
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    if dfs(neighbour):
                        return True  # Short-circuit if destination is found
            return False

        return dfs(source)
        
