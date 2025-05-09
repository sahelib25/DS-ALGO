class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s+s

        # if len(s) != len(goal):
        #     return False
        # else:
        #     var = s + s
        #     if goal in var:
        #         return True
        #     else:
        #         return False
        
        
