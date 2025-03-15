class Solution:
    def rob(self, nums: List[int]) -> int:
        def maxMoney(nums):
            house1, house2 = 0, 0
            for num in nums:
                curr = max(num + house1, house2)
                house1 = house2
                house2 = curr

            return house2

        # nums[0] cause edge case what if we only had 1 number
        return max(nums[0], maxMoney(nums[1:]), maxMoney(nums[:-1]))