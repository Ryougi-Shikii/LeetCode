# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:

        def treeHeight(root):
            if not root:
                return 0
            lh = treeHeight(root.left)
            rh = treeHeight(root.right)
            return 1 + max(lh, rh)
        
        return treeHeight(root)
        