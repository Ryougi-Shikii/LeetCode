# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        def cbst(list_sorted):
            if not list_sorted:
                return
            mid=(len(list_sorted))//2
            root = TreeNode(list_sorted[mid])

            root.left=cbst(list_sorted[:mid])
            root.right=cbst(list_sorted[mid+1:])
            return root
        return cbst(nums)
            