import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            left_stone = -heapq.heappop(stones)
            right_stone = -heapq.heappop(stones)

            if left_stone < right_stone:
                heapq.heappush(stones, left_stone - right_stone)
            elif left_stone > right_stone:
                heapq.heappush(stones, right_stone - left_stone)
            else:
                continue
        if stones:
            return -stones[0]
        return 0