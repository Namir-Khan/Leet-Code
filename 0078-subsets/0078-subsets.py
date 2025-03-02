class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            ret.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])

                backtrack(i + 1, path)
                path.pop()
        
        ret = []
        backtrack(0, [])
        return ret