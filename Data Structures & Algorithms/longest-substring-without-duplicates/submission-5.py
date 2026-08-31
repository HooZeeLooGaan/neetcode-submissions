class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        res = 0
        left = 0
        right = 0
        while right < len(s):
            if s[right] in count:
                res = max(res, right - left)
                left = max(left, count[s[right]] + 1)
            count[s[right]] = right
            right += 1
        return max(res, right - left)