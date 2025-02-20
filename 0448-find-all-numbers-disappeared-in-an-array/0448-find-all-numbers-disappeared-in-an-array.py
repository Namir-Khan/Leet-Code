class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        x = set(range(1,len(nums)+1))
        y = set(nums)
        return list(x.difference(y))