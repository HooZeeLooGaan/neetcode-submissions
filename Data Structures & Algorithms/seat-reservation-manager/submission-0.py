import heapq

class SeatManager:
    def __init__(self, n: int):
        self.min_heap = list(range(1, n + 1))
        heapq.heapify(self.min_heap)

    def reserve(self) -> int:
        seat = heapq.heappop(self.min_heap)
        return seat
        
    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.min_heap, seatNumber)
