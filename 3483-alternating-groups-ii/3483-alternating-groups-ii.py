class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        ret, l = 0, 0
        n = len(colors)

        for r in range(n + k - 1):
            if colors[r % n] == colors[(r + 1) % n]:
                l = r
            if r - l + 1 > k:
                l += 1
            if r - l + 1 == k:
                ret += 1
            
        return ret