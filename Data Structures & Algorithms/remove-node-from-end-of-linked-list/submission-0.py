from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first, second = head, head
        
        for _ in range(n):
            second = second.next

        if second is None:
            return head.next

        prev = first
        print(second.val)
        while second.next is not None:
            second = second.next
            first = first.next

        first.next = first.next.next

        return head