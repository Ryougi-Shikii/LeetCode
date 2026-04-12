# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root) -> bool:
        res = []
        def treeHeight(node):
            if not node:
                return 0
            lh = treeHeight(node.left)
            rh = treeHeight(node.right)
            if abs(lh-rh)>1:
                res.append(False)
            return 1 + max(lh, rh)
        treeHeight(root)
        return False if False in res else True