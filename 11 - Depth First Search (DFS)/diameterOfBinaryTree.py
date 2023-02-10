# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        self.maxDiameter = 0
        self.dfs(root)
        return self.maxDiameter

    def dfs(self, node):
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.maxDiameter = max(self.maxDiameter, left + right)
        return 1 + max(left, right)

# Official solution

class Solution:
    def __init__(self):
        self.maxPath = 1

    def diameterOfBinaryTree(self, root):
        if root == None:
            return 0

        self.dfs(root)
        return self.maxPath - 1

    def dfs(self, root):
        if root == None:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.maxPath = max(self.maxPath, left + right + 1)

        return max(left, right) + 1
