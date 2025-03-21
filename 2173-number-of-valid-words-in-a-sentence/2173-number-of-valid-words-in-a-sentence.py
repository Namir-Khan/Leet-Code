class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split()
        count = 0

        for word in words:
            if any(ch.isdigit() for ch in word):
                continue
            
            if len(word) == 1:
                if word.isalpha() or word in "!.,":  
                    count += 1
                continue  

            hyphen_count = 0
            for i, ch in enumerate(word):
                if ch == '-':
                    hyphen_count += 1
                    if hyphen_count > 1 or i == 0 or i == len(word) - 1 or not (word[i - 1].isalpha() and word[i + 1].isalpha()):
                        break  
                if ch in "!.,":  
                    if i != len(word) - 1:
                        break
            else:
                count += 1

        return count