class Solution {
public:
    void reverseString(vector<char>& s) {
        int start;
        int end;
        char temp;
        start = 0;
        end = s.size()-1;
        while(start<end){
                swap(s[start],s[end]);
                start ++;
                end --; 
        }

    }
};