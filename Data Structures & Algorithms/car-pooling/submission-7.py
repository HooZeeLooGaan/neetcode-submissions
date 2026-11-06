import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        space = capacity
        min_heap = []
        trips.sort(key= lambda x:x[1])

        for trip in trips:            
            while min_heap and trip[1] >= min_heap[0][0]:
                previous_trip = heapq.heappop(min_heap)
                space += previous_trip[1]
            
            heapq.heappush(min_heap, (trip[2], trip[0]))
            space -= trip[0]
            if space < 0:
                print(trip, space)
                return False

        return True