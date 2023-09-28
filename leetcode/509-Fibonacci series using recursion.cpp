class Solution {
public:
    int fib(int n) {
        if (n==0 || n==1){
            return n;
        }
        return fib(n-1) + fib(n-2);
    }
};

// Using Dynamic programming
// class Solution {

// public: 
//     int calc(vector<int>& dp, int n){
//         if (n<=1){
//             return n;
//         }
//         if(dp[n] != -1){
//             return dp[n];
//         }
//         return calc(dp, n-1) + calc(dp, n-2);
//     }
// public:
//     int fib(int n) {
//         vector<int> dp(n+1, -1);
        
//         return calc(dp,n);
//     }
// };