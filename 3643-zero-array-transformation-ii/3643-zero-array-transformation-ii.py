class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # We use the consept of difference array or say relative difference (LC:370)
        n = len(nums)
        diff = [0] * (n + 1)
        sum_val = 0
        pos = 0
        
        for i in range(n):
            while sum_val + diff[i] < nums[i]:
                if pos == len(queries):  # All Queries done?
                    return -1
                
                start, end, val = queries[pos]
                pos += 1
                
                if end < i:  # Skip past update
                    continue
                
                # Range update in O(1)
                diff[max(start, i)] += val
                if end + 1 < n:
                    diff[end + 1] -= val
            
            sum_val += diff[i]
        
        return pos
            