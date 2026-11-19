class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # initialize 2 pointers for each string
        # traverse haystack pointer
        # move needle pointer if there is character match
        # else assign needle pointer to 0
        if not needle:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i

        return -1
