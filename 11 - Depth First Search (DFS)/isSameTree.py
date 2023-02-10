# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p, q):
        if (q and not p) or (p and not q) or (q and p and q.val != p.val):
            return False
        if not q and not p:
            return True
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
# Official solution

class Solution:
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True

        if p == None or q == None:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
