# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root, targetSum):
        if not root: return []
        self.paths = []
        path = [root.val]
        self.dfs(root, targetSum, path)
        return self.paths
        
    def dfs(self, node, targetSum, path):
        if not node:
            return
        targetSum -= node.val
        if not node.left and not node.right and targetSum == 0:
            self.paths.append(path)
            return
        if node.left:
            self.dfs(node.left, targetSum, path + [node.left.val])
        if node.right:
            self.dfs(node.right, targetSum, path + [node.right.val])
            
# Official solution

class Solution:
    def pathSum(self, root, targetSum):
        output = []

        self.dfs(root, targetSum, [], output)

        return output

    def dfs(self, root, targetSum, currentPath, output):
        if root == None:
            return

        if root.left == None and root.right == None and targetSum == root.val:
            output.append(currentPath + [root.val])

        currentPath = currentPath + [root.val]
        targetSum = targetSum - root.val
        self.dfs(root.left, targetSum, currentPath, output)
        self.dfs(root.right, targetSum, currentPath, output)
