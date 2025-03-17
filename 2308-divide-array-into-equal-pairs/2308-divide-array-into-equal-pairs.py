class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)

        for num, c in count.items():
            if not c % 2 == 0:
                return False

        return True