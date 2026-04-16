# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        def returning(queue):
            resultingqueue = []
            ans = []
            while queue:
                cur = queue.pop(0)
                if cur is not None:
                    resultingqueue.append(cur.left)
                    resultingqueue.append(cur.right)
                    ans.append(cur.val)
            return (ans, resultingqueue)
        res = []
        queue = [root]
        while queue:
            ans, queue = returning(queue)
            res.append(ans)
        res.pop()

        res2 = []
        for i in res:
            res2.append(i[-1])
        
        return res2
        