class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies) # O(n)
        if total < k:
            return 0

        l, r = 1, total // k
        maxCandies = 0

        while l <= r: # O(log(total // k))
            count = 0
            m = (l + r) // 2

            for c in candies: # O(n)
                if c >= m:
                    count += c // m
                if count >= k:
                    break
            if count >= k:
                maxCandies = m
                l = m + 1
            else:
                r = m - 1

        return maxCandies