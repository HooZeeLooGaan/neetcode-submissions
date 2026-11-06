# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        res = current = ListNode(0)
        for list_node in lists:
            if list_node:
                heapq.heappush(min_heap, list_node)
        
        while min_heap:
            least_node = heapq.heappop(min_heap)
            current.next = least_node
            current = current.next

            if least_node.next:
                least_node = least_node.next
                heapq.heappush(min_heap, least_node)

        return res.next