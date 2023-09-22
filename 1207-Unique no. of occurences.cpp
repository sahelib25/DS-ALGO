class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {

    //declare an unordered map to store the array elements and the number of frequencies of each of the element

        unordered_map<int,int>mp;
        for (auto i:arr){
            mp[i]++;
        }
        
    // declare a set to find the unique elements
        unordered_set<int>s;
        for (auto j:mp){
            s.insert(j.second);
        }

    // compare the size of the unorered_map and the set
        if (mp.size()==s.size()) return true;
        else return false;
    }
};