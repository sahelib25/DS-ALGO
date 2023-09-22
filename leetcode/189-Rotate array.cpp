class Solution {
public:
    void rotate(vector<int>& nums, int k) {

        // declare a vector temp of size n
        vector<int> temp(nums.size());
        int n = nums.size();
        for (int i=0; i<n ; i++){
            temp[(i+k)%n] = nums[i];
        }
        nums = temp;

    }
};