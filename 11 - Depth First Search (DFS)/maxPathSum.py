# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root):
        self.maxSum = -float("inf")
        self.dfs(root)
        return self.maxSum

    def dfs(self, node):
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.maxSum = max(self.maxSum, left + right + node.val)
        res = max(max(left, right) + node.val, node.val)
        return res if res > 0 else 0
        
# Official solution

class Solution:
    def __init__(self):
        self.maxSum = 0

    def maxPathSum(self, root):
        self.maxSum = float("-inf")

        self.maxGain(root)

        return self.maxSum

    def maxGain(self, root):
        if root == None:
            return 0

        leftGain = max(self.maxGain(root.left), 0)
        rightGain = max(self.maxGain(root.right), 0)

        currentPathGain = root.val + leftGain + rightGain
        self.maxSum = max(self.maxSum, currentPathGain)

        return root.val + max(leftGain, rightGain)
