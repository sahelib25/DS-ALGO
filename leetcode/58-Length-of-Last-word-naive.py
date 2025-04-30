class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        len_s = len(s) - 1
        count = 0
        flag = False
        for i in range(len_s, -1, -1):
            if s[i] != ' ':
                count+=1
                flag = True
            elif flag:
                break
        return count