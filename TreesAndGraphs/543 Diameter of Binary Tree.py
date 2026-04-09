# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        res = [0]

        def rec(root):
            if not root:
                return 0
            
            lh = rec(root.left)
            rh = rec(root.right)

            res[0] = max(res[0], lh + rh)

            return 1 + max(lh, rh)

        rec(root)
        
        return res[0]