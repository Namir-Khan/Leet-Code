class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Here we use heapq lib to solve this and its function nlargest and nsmallest
        return heapq.nlargest(k, nums)[-1]