class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        long long num=0;
        long long temp = x;
        while(temp!=0){
            int digit = temp %10;
            num = num * 10 + digit;
            temp /= 10;
        }

        if (num==x) return true;
        else return false; 
    }
};