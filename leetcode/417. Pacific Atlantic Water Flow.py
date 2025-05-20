class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows = len(heights)
        cols = len(heights[0])
        ans = []

        pac, atl = set(), set()

        if not heights or not heights[0]:
            return []

        def dfs(r,  c, visit, prevHeight):
            if r<0 or c<0 or r>=rows or c>=cols:
                return
            if (r,c) in visit or heights[r][c] < prevHeight:
                return 

            visit.add((r,c))
            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:
                dfs(r + dr, c + dc, visit, heights[r][c])

        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1,c,atl,heights[rows-1][c])

        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,cols-1,atl,heights[r][cols-1])

        # ans = list(pac & atl)

        # or we can loop over all the cells those are in pac and atl both then add to ans
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    ans.append([r,c])
        return ans

            
