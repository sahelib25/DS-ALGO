
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        h_map = { chr(i + ord('a')) : str(i+1) for i in range (26)}

        num_str = ''.join(h_map[char] for char in s)

        for _ in range (k):
            num_str = str(sum(int(d) for d in num_str))

        return int(num_str)
    
