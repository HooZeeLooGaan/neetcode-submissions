from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_depth = 0
    
    def depthTraversal(self, root: Optional[TreeNode]):
        if not root:
            return 0
        level_depth = max(self.depthTraversal(root.left) + 1, self.depthTraversal(root.right) + 1)
        self.max_depth = max(level_depth, self.max_depth)
        return level_depth
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.depthTraversal(root)
        return self.max_depth