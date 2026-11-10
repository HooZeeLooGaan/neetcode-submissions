from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        frequency = list(Counter(nums).values())
        operations = 0
        for freq in frequency:
            if freq == 1:
                return -1
            if freq % 3 == 0:
                operations += freq//3
            elif freq % 3 == 1:
                operations += freq//3 + 1
            elif freq % 3 == 2:
                operations += freq//3 + 1

        return operations


