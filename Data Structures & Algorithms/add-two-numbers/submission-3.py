# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        rem = 0
        l3_head = l3
        while l1 is not None and l2 is not None:
            sum = rem + l1.val + l2.val
            rem = sum // 10
            l3.next = ListNode(sum % 10)

            l1 = l1.next
            l2 = l2.next
            l3 = l3.next
        
        while l1:
            sum = rem + l1.val
            rem = sum // 10
            l3.next = ListNode(sum % 10)
            l1 = l1.next
            l3 = l3.next

        while l2:
            sum = rem + l2.val
            rem = sum // 10
            l3.next = ListNode(sum % 10)
            l2 = l2.next
            l3 = l3.next


        if rem > 0:
            l3.next = ListNode(rem)

        return l3_head.next