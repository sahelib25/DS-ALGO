class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # hashmap = defaultdict(int)

        # for i,j in edges:
        #     hashmap[i] += 1
        #     hashmap[j] += 1


        # nodes = len(edges) +1
        # for idx in range(1, nodes +1):
        #     if hashmap[idx] == nodes -1:
        #         return idx
        
        a, b = edges[0]
        c, d = edges[1]
        return a if a in (c, d) else b
