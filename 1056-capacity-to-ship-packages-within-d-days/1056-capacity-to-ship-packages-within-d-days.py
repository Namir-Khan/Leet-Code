class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        minCap = r

        def canShip(m):
            shipCount, currCap = 1, m
            for w in weights:
                if currCap - w < 0:
                    shipCount += 1
                    currCap = m
                currCap -= w

            return shipCount <= days

        while l <= r:
            m = (l + r) // 2
            if canShip(m):
                minCap = min(minCap, m)
                r = m - 1
            else:
                l = m + 1

        return minCap