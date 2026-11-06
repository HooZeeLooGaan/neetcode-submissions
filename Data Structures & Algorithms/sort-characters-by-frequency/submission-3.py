from collections import Counter
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        count_dict = Counter(s)

        max_heap = []
        for alpha in count_dict:
            heapq.heappush(max_heap, (-count_dict[alpha], alpha))
        
        res = ""
        while max_heap:
            count, alpha = heapq.heappop(max_heap)
            res += (alpha * -count)
        return res