class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        
        // edge condition
        if(nums.empty())return {};

        // declare unorderd map
        unordered_map<int,int>mp;

        //declare ans to store the resultant vector
        vector<int>ans;

        for (auto i:nums){
            mp[i]++;
        }

        // check which elements in the unordered map have frequencies equals to 2
        for( auto i:mp){
            if(i.second == 2){
             
            // store them to ans 
            ans.push_back(i.first);
            }
        }

        //return ans
        return ans;

    }
};