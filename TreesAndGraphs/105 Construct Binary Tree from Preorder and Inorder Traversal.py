# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        mid = inorder.index(preorder[0])
        root = TreeNode(preorder[0])

        # inorder -> left inorder[:mid] right inorder[mid+1:]
        # preorder -> left preorder[1: 1+len(inorder_left)] right preorder[1+len(inorder_left):]
        inorder_left = inorder[:mid]
        inorder_right = inorder[mid+1:]
        preorder_left = preorder[1: 1+len(inorder_left)]
        preorder_right = preorder[1+len(inorder_left):]

        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        
        return root