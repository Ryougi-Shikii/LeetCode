# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
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
        i = 0
        while queue:
            ans, queue = returning(queue)
            if i%2==0:
                res.append(ans)
            else:
                res.append(ans[::-1])
            i+=1
        res.pop()
        #print(res)
        return res