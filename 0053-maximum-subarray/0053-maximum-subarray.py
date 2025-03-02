class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        for i, v in enumerate(nums):
            dp[i] = max(v, v + dp[i-1])

        return max(dp)