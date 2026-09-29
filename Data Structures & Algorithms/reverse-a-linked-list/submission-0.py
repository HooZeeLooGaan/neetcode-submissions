from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None

    def _revList(self, node: Optional[ListNode]):
        if node is None or node.next is None:
            self.head = node
            return node
        curr_node = self._revList(node.next)
        curr_node.next = node
        node.next = None
        print(curr_node.val)
        return node
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self._revList(head)
        return self.head