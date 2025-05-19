class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        original_color = image[sc][sr]

        if original_color == color:
            return image

        visit = set()

        def dfs(i,j):
            visit.add((i,j))
            if i >= rows or j >= cols or j<0 or i<0 or image[i][j]!= original_color:
                return
            
            image[i][j] = color
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i+1,j)

        dfs(sr,sc)
        return image
        
