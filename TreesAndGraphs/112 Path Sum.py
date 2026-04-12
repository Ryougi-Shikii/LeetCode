# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        # its not dp but it may look like !!! -> its dfs with state check propogation !!!
        def dp(root, targetSum):
            if not root:
                return False
            if not root.left and not root.right:
                return targetSum == root.val
            left = dp(root.left, targetSum-root.val)
            right = dp(root.right, targetSum-root.val)
            return left or right
        
        return dp(root, targetSum)