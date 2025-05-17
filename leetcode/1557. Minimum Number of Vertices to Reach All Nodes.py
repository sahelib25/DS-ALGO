class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # Find vertices with no incoming edges
        res = []
        incoming = defaultdict(int)

        for u,v in edges:
            incoming[v] += 1
        
        for i in range(0,n):
            if incoming[i] == 0:
                res.append(i)
        return res
