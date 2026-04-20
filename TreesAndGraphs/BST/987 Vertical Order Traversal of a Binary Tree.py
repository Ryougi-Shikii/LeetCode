# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root):
        first = dict()
        que = [(root, 0, 0)]
        while que:
            sz = len(que)
            newque = []
            second = dict()
            for _ in range(sz):
                node, row, col = que.pop(0)
                if node:
                    if col not in second:
                        second[col] = []
                    second[col] += [node.val]
                    newque.append((node.left, row+1, col-1))
                    newque.append((node.right, row+1, col+1))
            for k,v in second.items():
                v = sorted(v)
                if k not in first:
                    first[k] = []
                first[k] += v
            que = newque[:]
        res = []
        for k in sorted(first.keys()):
            res.append(first[k])
        return res
