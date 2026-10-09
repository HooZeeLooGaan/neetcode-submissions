class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = [k]
        result = [0]
        
        def inorder(node: Optional[TreeNode]):
            if not node or counter[0] == 0:
                return

            inorder(node.left)

            counter[0] -= 1
            if counter[0] == 0:
                result[0] = node.val
                return 

            inorder(node.right)

        inorder(root)
        return result[0]