from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        max_count = 0
        odd = False

        for item, frequency in counter.items():
            if frequency % 2 == 0:
                max_count += frequency
            
            else:
                max_count += frequency - 1
                if not odd:
                    max_count += 1
                    odd = True
        
        return max_count