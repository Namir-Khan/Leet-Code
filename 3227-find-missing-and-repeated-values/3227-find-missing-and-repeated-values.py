class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        hashmap = {}
        a, b = -1, -1
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] in hashmap:
                    hashmap[grid[i][j]] += 1
                    a = grid[i][j]
                else:
                    hashmap[grid[i][j]] = 1
        
        for i in range(1, len(grid)**2 + 1):
            if i in hashmap:
                continue
            else:
                b = i
        
        return [a, b]