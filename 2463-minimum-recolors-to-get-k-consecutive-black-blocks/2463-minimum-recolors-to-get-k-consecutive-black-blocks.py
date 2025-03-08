class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minChanges = k # We could set this as k as well cause its gonna be the max changes
        currChanges = 0
        l = 0
        for r in range(len(blocks)):
            if blocks[r] == 'W':
                currChanges += 1
            if r - l + 1 == k:
                minChanges = min(minChanges, currChanges)
                if blocks[l] == 'W':
                    currChanges -= 1
                l += 1

        return minChanges