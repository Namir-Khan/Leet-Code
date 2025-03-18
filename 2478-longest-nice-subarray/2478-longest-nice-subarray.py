class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0
        bitmask = 0
        maxCount = 1

        for r in range(len(nums)):
            while bitmask & nums[r]:
                bitmask ^= nums[l]
                l += 1

            bitmask |= nums[r]
            maxCount = max(maxCount, r - l + 1)

        return maxCount