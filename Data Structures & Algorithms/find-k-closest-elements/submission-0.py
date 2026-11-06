import heapq
import math

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        max_heap = []
        for element in arr:
            distance = math.fabs(x - element)
            heapq.heappush(max_heap, (-distance, -element))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        res = []
        print(max_heap)
        while max_heap:
            _, element = heapq.heappop(max_heap)
            res.append(-element)
        return sorted(res)
