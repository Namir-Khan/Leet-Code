class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, end):
            if start == end:
                ret.append(nums[:])
                return
            
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1, end)
                nums[start], nums[i] = nums[i], nums[start]
                

        ret = []
        backtrack(0, len(nums))

        return ret