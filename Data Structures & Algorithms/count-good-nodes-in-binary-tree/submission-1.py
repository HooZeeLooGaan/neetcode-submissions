from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:        
    def goodNodes(self, root: TreeNode) -> int:
        def recursiveDepthTraversal(node: TreeNode, max_so_far: int) -> int:
            if not node:
                return 0

            count = 1 if node.val >= max_so_far else 0
            new_max = max(max_so_far, node.val)
            
            count += recursiveDepthTraversal(node.left, new_max)
            count += recursiveDepthTraversal(node.right, new_max)

            return count
                
        return recursiveDepthTraversal(root, root.val) 