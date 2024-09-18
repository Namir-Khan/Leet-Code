class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size();
        // Find pivot element
        int i = n-2;
        while(i >= 0 && nums[i] >= nums[i+1]) {
            i--;
        }

        // Swap the pivot with the smallest element after the pivot
        if(i >= 0){
            int j = n - 1;
            while(j >= 0 && nums[j] <= nums[i]){
                j--;
            }
            swap(nums[i], nums[j]);
        }

        // Reverse the array after the pivot till the end
        reverse(nums.begin() + i + 1, nums.end());
    }
};