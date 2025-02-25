class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = deque()
        lp, rp = 0, len(nums) - 1

        while lp <= rp:
            lv, rv = abs(nums[lp]), abs(nums[rp])
            if lv > rv:
                ans.appendleft(lv * lv)
                lp += 1
            else:
                ans.appendleft(rv * rv)
                rp -= 1

        return list(ans)
