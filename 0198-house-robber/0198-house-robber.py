class Solution:
    def rob(self, nums: List[int]) -> int:
        # This is a brute force approach O(2^n)
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
        #     return max(dfs(i + 1),
        #                nums[i] + dfs(i + 2))
        
        # return dfs(0)

        # Dynamic approach O(n)
        # [....., house1, house2, num, num+1, ...]
        house1, house2 = 0, 0
        for num in nums:
            curr = max(num + house1, house2)
            house1 = house2
            house2 = curr

        return house2