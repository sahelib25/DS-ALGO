class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visit = set()
        n = len(isConnected)
        adj_list = [ [] for _ in range(n) ]

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i!=j:
                    adj_list[i].append(j)

        def dfs(node):
            visit.add((node))
            
            for neighbour in adj_list[node]:
                if neighbour not in visit:
                    dfs(neighbour)

        provinces = 0
        for city in range(n):
            if city not in visit:
                dfs(city)
                provinces +=1

        return provinces 

                 
