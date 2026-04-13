# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root == p or root ==q or root == None:
            return root

        lcaleft = self.lowestCommonAncestor(root.left, p, q)
        lcaright = self.lowestCommonAncestor(root.right, p, q)
        if lcaleft != None and lcaright != None:
            return root
        if lcaleft == None:
            return lcaright
        return lcaleft