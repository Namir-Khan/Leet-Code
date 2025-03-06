class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while k > 0 and stack and stack[-1] > c:
                k -= 1
                stack.pop()
            stack.append(c)

        stack = stack[:len(stack) - k] # To remove the extra elements
        res = "".join(stack) # Stack to a string

        # Remove leading 0's
        res = res.lstrip("0")
        
        return res if res else "0"