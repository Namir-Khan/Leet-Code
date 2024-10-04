// Here we 1st check if the number is a start of a sequence
// Then after we do that we check if the next number is present if yes count++
// Max count display

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int>s(nums.begin(), nums.end());
        int longest = 0;
        for(auto &n: s){
            if(!s.count(n - 1)){
                int length = 1; 
                while(s.count(n + length))
                    ++length;
                longest = max(longest, length);
            }
        }
        return longest;
    }
};