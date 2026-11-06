class MedianFinder:

    def __init__(self):
        self.right_min_heap = []
        self.left_max_heap = []        

    def _isTreeBalanced(self) -> int:
        if len(self.left_max_heap) == len(self.right_min_heap):
            return 0
        if len(self.left_max_heap) > len(self.right_min_heap):
            return -1
        return 1

    def _rebalanceTree(self, skewness: int) -> None:
        if skewness == 1:
            top = heapq.heappop(self.right_min_heap)
            heapq.heappush(self.left_max_heap, -top)
        elif skewness == -1:
            top = heapq.heappop(self.left_max_heap)
            heapq.heappush(self.right_min_heap, -top)
        return

    def addNum(self, num: int) -> None:
        median = self.findMedian()
        
        if num <= median:
            heapq.heappush(self.left_max_heap, -num)
            self._rebalanceTree(self._isTreeBalanced())
            
        else:
            heapq.heappush(self.right_min_heap, num)
            self._rebalanceTree(self._isTreeBalanced())

    def findMedian(self) -> float:
        if not self.left_max_heap and not self.right_min_heap:
            return 0

        balancedTree = self._isTreeBalanced()
        match balancedTree:
            case 0:
                return (-self.left_max_heap[0] + self.right_min_heap[0])/2
            case 1:
                return self.right_min_heap[0] 
            case -1:
                return -self.left_max_heap[0]

        return 0   