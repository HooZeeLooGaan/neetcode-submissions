class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = {}
        tCount = {}
        
        for i in range(max(len(s), len(t))):
            if i < len(s):
                sCount[s[i]] = sCount.get(s[i],0) + 1
            if i < len(t):
                tCount[t[i]] = tCount.get(t[i],0) + 1

        if (sorted(sCount.items()) == sorted(tCount.items())):
            return True
        return False
        