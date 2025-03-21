class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        max_len, zero_count, one_count = 0, 0, 0
        
        for i in range(len(s)):
            if s[i] == '0':  
                if i > 0 and s[i - 1] == '1':  
                    zero_count = 0
                    one_count = 0
                zero_count += 1  

            else:  # s[i] == '1'
                one_count += 1
                max_len = max(max_len, 2 * min(zero_count, one_count))

        return max_len