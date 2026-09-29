from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()
        curr_node = list3
        
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                curr_node.next = list1
                list1 = list1.next
            else:
                curr_node.next = list2
                list2 = list2.next
            curr_node = curr_node.next

        if list1 is not None:
            curr_node.next = list1
        if list2 is not None:
            curr_node.next = list2
        
        return list3.next