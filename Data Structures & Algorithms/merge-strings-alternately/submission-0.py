class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3 = ''
        p = 0
        for p in range(0, min(len(word1), len(word2))):
            word3 += word1[p] + word2[p]
            p += 1

        if len(word1) > p:
            word3 += word1[p:]

        if len(word2) > p:
            word3 += word2[p:]

        return word3