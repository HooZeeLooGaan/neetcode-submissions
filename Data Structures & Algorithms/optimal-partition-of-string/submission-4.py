from collections import Counter

class Solution:
    def partitionString(self, s: str) -> int:
        track = {}
        substrings = 0
        for char in s:
            if char in track:
                track = {char: 1}
                substrings += 1

            else:
                track[char] = 1

        if track:
            substrings += 1
        return substrings

