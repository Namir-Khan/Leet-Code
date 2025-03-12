class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        nCount, pCount = 0, 0
        for num in nums:
            if num < 0:
                nCount += 1
            elif num > 0:
                pCount += 1

        return max(nCount, pCount)