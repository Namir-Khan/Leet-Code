class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def maxSubArr(arr):
            dp = [0] * len(nums)

            for i, v in enumerate(arr):
                dp[i] = max(v, v+dp[i-1])

            return max(dp)

        # maxSum = maxSubArr(nums)

        # for i in range(len(nums) - 1):
        #     nums.append(nums.pop(0))
        #     maxSum = max(maxSum, maxSubArr(nums))

        # return maxSum

        # This method works but is 0(N2)  Time Complexity so No no no no nooo

        maxSum = maxSubArr(nums)
        minSum = maxSubArr([-num for num in nums])
        total = sum(nums)

        if maxSum < 0:
            return maxSum

        return max(maxSum, total + minSum)