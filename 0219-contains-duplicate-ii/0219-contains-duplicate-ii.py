class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Can be done using sliding window as well with sets
        map = {}
        for i, v in enumerate(nums):
            if v in map and (abs(i - map[v]) <= k):
                return True
            map[v] = i
        
        return False