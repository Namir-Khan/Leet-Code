class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atleastk(k):
            res, l = 0, 0
            count = defaultdict(int)

            for r in range(len(nums)):
                count[nums[r]] += 1 # Here we count till we get atleast k int then below loop

                while len(count) >= k:
                    # This is basically that valid substr + all the str if we add the next digit in it
                    res += len(nums) - r

                    # Now after calculating we inc the left pointer
                    count[nums[l]] -= 1
                    if count[nums[l]] == 0: # To keep the count of int correct we pop
                        count.pop(nums[l])
                    l += 1

            return res

        # This is basically eg >=3 and >=4 and sub to get exactly 3 (Take eg 2 on paper)
        return atleastk(k) - atleastk(k + 1)