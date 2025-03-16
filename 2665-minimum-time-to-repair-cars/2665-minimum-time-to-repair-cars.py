class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        n = len(ranks)
        l, r = 1, ranks[0] * cars * cars

        def count_rep(time):
            count = 0
            for r in ranks:
                count += int(sqrt(time / r))
            return count

        res = -1
        while l <= r:
            m = (l + r) // 2
            repaired = count_rep(m)
            if repaired >= cars:
                res = m
                r = m - 1
            else:
                l = m + 1

        return res