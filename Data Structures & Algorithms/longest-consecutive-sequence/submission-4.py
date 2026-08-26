class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        seq = sorted(list(set(nums)))
        maxvalue = 1
        c = 1
        for i in range(1, len(seq)):
            c = c + 1 if seq[i] == seq[i-1] + 1 or seq[i] + 1 == seq[i-1]  else 1      
            maxvalue = max(maxvalue, c)
        return maxvalue