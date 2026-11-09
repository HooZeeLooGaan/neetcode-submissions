class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i = j = 0
        content_children = 0
        g.sort()
        s.sort()
        
        print(g, s)
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                content_children += 1
                i += 1
                j += 1

            while j < len(s) and i < len(g) and g[i] > s[j]:
                j += 1
                

        return content_children
