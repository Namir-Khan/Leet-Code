class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        map = {}
        ret = []
        n2 = sorted(nums)
        for i,v in enumerate(n2):
            if v not in map:
                map[v] = i

        for i in nums:
            ret.append(map[i])

        return ret