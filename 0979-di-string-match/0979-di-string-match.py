class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        li = [i for i in range(len(s) + 1)]
        res = []

        for c in s:
            if c == 'I':
                res.append(li[0])
                li.pop(0)
            else:
                res.append(li[-1])
                li.pop(-1)
        

        return res + li