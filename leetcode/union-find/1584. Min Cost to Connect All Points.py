class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        
    def find(self, x):
        if self.parent[x] !=x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr , yr = self.find(x) , self.find(y)

        if xr == yr:
            return False
        if self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
        elif self.rank[yr] < self.rank[xr]:
            self.parent[yr] = xr
        else:
            self.parent[yr] = xr
            self.rank[xr] += 1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = DSU(n)
        edges = []

        for i in range(n):
            for j in range(i+1, n):
                x1 , y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                edges.append((dist,i,j))

        edges.sort(key=lambda x: x[0])
        mst = 0
        edges_used = 0

        for dist,u,v in edges:
            if dsu.union(u,v):
                mst += dist
                edges_used += 1
                print(mst)
                if edges_used == n-1:
                    break
        return mst


        