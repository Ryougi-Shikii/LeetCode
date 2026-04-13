# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        # psi / pei -> preorder starting / ending index
        # isi / iei -> inorder starting / ending index
        def f(psi, pei, isi, iei):
            if psi>pei or isi>iei: return None
            root = TreeNode(preorder[psi])
            i=isi
            while inorder[i] != root.val:
                i+=1
            lstnodes = i - isi
            root.left = f(psi + 1, psi + lstnodes, isi, i-1)
            root.right = f(psi + lstnodes +1, pei, i+1, iei)
            return root
        return f(0, len(preorder)-1, 0, len(inorder)-1)