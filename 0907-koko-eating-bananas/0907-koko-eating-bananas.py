class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        l, r = 1, max(piles)
        minK = 0

        while l <= r:
            m = (l + r) // 2
            count = 0

            for p in piles:
                count += math.ceil(p / m)
                if count > h:
                    l = m + 1
                    break

            if count <= h:
                r = m - 1
                minK = m

        return minK