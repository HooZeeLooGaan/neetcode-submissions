# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}
        pre_idx = [0]
        def constructTree(left: int, right: int):
            if left > right:
                return None
            root_val = preorder[pre_idx[0]]
            root = TreeNode(root_val)
            pre_idx[0] += 1

            idx = inorder_map[root_val]

            root.left = constructTree(left, idx - 1)
            root.right = constructTree(idx + 1, right)

            return root

        return constructTree(0, len(inorder) - 1)