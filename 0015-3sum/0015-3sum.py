class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet = []
        nums.sort()

        for i, v in enumerate(nums):

            #Check for doubles
            if i>0 and v == nums[i-1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:

                currSum = v + nums[l] + nums[r]
                if currSum > 0:
                    r -= 1
                elif currSum < 0:
                    l += 1
                else: # Now we do operations when its 0
                    triplet.append([v, nums[l], nums[r]])

                    # Conti. this operation to find more
                    l += 1
                    while(l < r and nums[l] == nums[l-1]):
                        l += 1

        return triplet