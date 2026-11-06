import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        min_heap = []
        for i, num in enumerate(nums):
            heapq.heappush(min_heap, (num, i))

        while k > 0:
            min_ele, idx = heapq.heappop(min_heap)
            heapq.heappush(min_heap, (min_ele * multiplier, idx))
            k -= 1
            
        min_heap.sort(key = lambda x:x[1])
        return [x for x, _ in min_heap]