class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 1. We dont need visit set as we are going to get the cells and check for 1's
        # We can call DFS on a starting node, so need to find a cell with a value 1

        rows = len(grid)
        cols = len(grid[0])

        def dfs(i,j):
            if i>= rows or j>=cols or i<0 or j<0 or grid[i][j] !=1:
                return 0
            
            grid[i][j] = 0
            area = 1
            area += dfs(i-1,j)
            area += dfs(i+1,j)
            area += dfs(i,j+1)
            area += dfs(i,j-1)

            return area

        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i,j))
                    
        return max_area
