class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
      # apply Dijktra's algorithm
        adj_list = [[] for _ in range(n+1)]

        for u,v,w in times:
            adj_list[u].append([v,w])

        dist = [float('inf') for i in range(n+1)]
        dist[k]=0
        pq = [(0,k)]

        while pq:
            cur_dist, u = heapq.heappop(pq)
            
            for v,w in adj_list[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v],v))
                    
        max_dist = max(dist[1:])

        return max_dist if max_dist!=float('inf') else -1
        


