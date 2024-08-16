class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        // Method 1 :- Brute Force i.e O(n^2)
        // Method 2 :- Sorting then check 2 at a time i.e O(nlogn)
        // Method 3 :- Using HashMap

        int n = nums.size();
        unordered_map<int, int> numMap;

        for(int i = 0; i < n; i++){
            numMap[nums[i]] = i;
        }

        for(int i = 0; i < n; i++){
            if(numMap.count(nums[i]) && numMap[nums[i]] != i){
                return true;
            }
        }
        return false;
    }
};