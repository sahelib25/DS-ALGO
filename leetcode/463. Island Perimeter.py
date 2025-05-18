class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        total_perimeter = 0
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    total_perimeter += 4 
                # Find the commonn edges and substract that from up and left:
                    if i>0 and grid[i-1][j]==1:
                        total_perimeter -= 2
                    if j>0 and grid[i][j-1]==1:
                        total_perimeter -=2
        return total_perimeter
