class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, path):
            if len(path) == k:
                ret.append(path[:])
                return

            for i in range(start, n+1):
                path.append(i)
                backtrack(i+1, path)
                path.pop()
        
        ret = []
        backtrack(1, [])

        return ret