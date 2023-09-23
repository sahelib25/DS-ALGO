class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t ans = 0;
        for (int i=0; i<32; i++){
            // left shift ans by 1 bit to place the last bit of n
            // ans is getting left shifted each time we are picking up the last bit from n 
            ans = (ans << 1) | (n&1);
            // n is right shifted each time to get the current last bit
            n = n >> 1;
        } 
        return ans;
    
    }
};