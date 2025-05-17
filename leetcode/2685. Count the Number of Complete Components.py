class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # number of edges in a connected component is (k * (k-1)) //2

        adj_list = [ [] for _ in range(n) ]
        visited = [False] * (n)
        # Make an ajacency list
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def dfs(node, nodes):
            visited[node] = True
            nodes.append(node)
            for neighbour in adj_list[node]:
                if not visited[neighbour]:
                    dfs(neighbour, nodes)

        count = 0

        for i in range(n):
            if not visited[i]:
                nodes = []
                dfs(i, nodes)
        
                #count edges in this component
                edges = 0
                for node in nodes:
                    edges += len(adj_list[node])
                edges //= 2  # because undirected graph counts edges twice

                v = len(nodes)
                expected_edges = (v * (v-1)) //2
                if edges == expected_edges:
                    count += 1

        return count 



