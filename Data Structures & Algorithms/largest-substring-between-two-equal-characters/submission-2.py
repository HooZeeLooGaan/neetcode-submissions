class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max_len = -1
        seen = {}

        for i, char in enumerate(s):
            if char in seen:
                max_len = max(max_len, i - seen[char] - 1)

            else:
                seen[char] = i

        return max_len