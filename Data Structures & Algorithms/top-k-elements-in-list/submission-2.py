from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i]+=1

        frequencies = sorted(count.values(), reverse=True)
        min_frequency_needed = frequencies[k - 1]
        result = [key for key, value in count.items() if value >= min_frequency_needed]
        
        return result
        