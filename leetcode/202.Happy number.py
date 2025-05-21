class Solution:
    def isHappy(self, n: int) -> bool:
        
        visit = set()

        while n!=1:
            if n in visit:
                return False

            visit.add(n)

            num_to_str = str(n)
            ans = 0
            for i in num_to_str:
                digit = int(i)
                ans += digit ** 2

            # 1 liner for loop : n = sum((int(digit) ** 2) for digit in num_to_str)

            n = ans
            
        return True # When n becomes 1
