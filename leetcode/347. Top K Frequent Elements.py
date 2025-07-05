class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)

        for num in nums:
            hash_map[num] += 1
        
        print(hash_map.get)
        return heapq.nlargest(k , hash_map.keys(), key=hash_map.get)
