class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # number of connected components
        visit = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i,j):
            if i<0 or j<0 or i>=rows or j>=cols or grid[i][j]!="1":
                return 0
            
            grid[i][j] = "0"
            count = 1
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for di,dj in directions:
                count += dfs(i+di, j+dj)

            return count 

        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1":
                    size = dfs(i,j)
                    islands += 1
        return islands

        
                

        
