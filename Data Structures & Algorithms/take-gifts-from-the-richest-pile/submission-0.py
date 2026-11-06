import heapq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = []
        for gift in gifts:
            heapq.heappush(max_heap, -gift)

        while k > 0:
            gift_in_hand = -heapq.heappop(max_heap)
            heapq.heappush(max_heap, -math.floor(math.sqrt(gift_in_hand)))
            k -= 1

        return -sum(max_heap)