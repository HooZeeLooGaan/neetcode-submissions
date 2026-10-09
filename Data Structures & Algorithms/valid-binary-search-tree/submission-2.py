from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recursiveDepthTraverse(node: Optional[TreeNode], low: float, high: float) -> bool:
            if not node:
                return True

            if not (low < node.val < high):
                return False

            return recursiveDepthTraverse(node.left, low, node.val) and recursiveDepthTraverse(node.right, node.val, high)

        return recursiveDepthTraverse(root, float('-inf'), float('inf'))