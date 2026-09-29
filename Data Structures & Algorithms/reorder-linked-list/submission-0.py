from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
            
        half, full = head, head.next
        while full and full.next:
            half = half.next
            full = full.next.next

        second = half.next
        half.next = None

        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2