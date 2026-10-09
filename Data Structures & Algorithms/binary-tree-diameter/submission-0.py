from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:        
        def traverseTree(node) -> int:
            if not node:
                return 0
            left_depth = traverseTree(node.left)
            right_depth = traverseTree(node.right)

            self.diameter = max(self.diameter, left_depth + right_depth)

            return 1 + max(left_depth, right_depth)
            
        traverseTree(root)
        return self.diameter