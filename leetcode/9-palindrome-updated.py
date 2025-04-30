class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False
        div = 1

        while x>=div*10:
            div = div * 10

        while x:
            right = x % 10 # get the rightmost digit 
            left= x // div # get the leftmost digit
            
            if left != right: return False

            x = (x % div) // 10 # chop off the left digit first then the right digit
            div = div / 100 # chopped off two digits so need to divide by 100

        return True