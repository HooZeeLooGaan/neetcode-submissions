import heapq
import math

class Solution:
    def GetEuclideanDistance(self, x: int, y: int) -> (int, list[list[int]]):
        d = math.sqrt(x**2 + y**2)
        return (-d, [x,y])


    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for x, y in points:
            heapq.heappush(max_heap, self.GetEuclideanDistance(x, y))

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [points for distance, points in max_heap]