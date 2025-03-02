class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        steps = [1, 2]

        for i in range(1, n+1):
            for s in steps:
                if i - s >= 0:
                    dp[i] += dp[i-s]

        return dp[-1] 