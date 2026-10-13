from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_map = Counter(nums)
        count_map = {value:key for key, value in count_map.items()}

        max_freq = max(count_map)
        if max_freq > len(nums)/2:
            return count_map[max_freq]
        return -1