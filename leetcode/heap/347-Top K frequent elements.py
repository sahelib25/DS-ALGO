class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        print(freq)

        return heapq.nlargest(k, freq.keys(), key=freq.get)