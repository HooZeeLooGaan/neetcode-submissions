class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.index = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index = 0
        node = head
        
        while node is not None:
            if node.index is not None:
                return True
                
            node.index = index
            index += 1
            node = node.next
        return False