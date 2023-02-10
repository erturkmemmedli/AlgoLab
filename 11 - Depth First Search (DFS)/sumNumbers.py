# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root):
        self.sum = 0
        self.dfs(root, 0)
        return self.sum

    def dfs(self, node, pathSum):
        if not node:
            return 0
        pathSum += node.val
        if not node.left and not node.right:
            self.sum += pathSum
        self.dfs(node.left, 10 * pathSum)
        self.dfs(node.right, 10 * pathSum)
        
# Official solution

class Solution:
    def __init__(self):
        self.output = 0

    def sumNumbers(self, root):
        self.preorder(root, 0)

        return self.output

    def preorder(self, root, currNumber):
        if root:
            currNumber = currNumber * 10 + root.val

            if not (root.left or root.right):
                self.output += currNumber

            self.preorder(root.left, currNumber)
            self.preorder(root.right, currNumber)
