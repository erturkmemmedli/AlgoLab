# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root, low, high):
        self.rangeSum = 0
        self.dfs(root, low, high)
        return self.rangeSum
        
    def dfs(self, node, low, high):
        if not node:
            return
        if node.val <= low:
            if node.val == low:
                self.rangeSum += node.val
            self.dfs(node.right, low, high)
        elif node.val >= high:
            if node.val == high:
                self.rangeSum += node.val
            self.dfs(node.left, low, high)
        else:
            self.rangeSum += node.val
            self.dfs(node.left, low, high)
            self.dfs(node.right, low, high)
            
# Official solution

class Solution:
    def rangeSumBST(self, root, low, high):
        if not root:
            return False

        inOrderTraversal = []

        self.inorder(root, inOrderTraversal)

        lowIndex = inOrderTraversal.index(low)
        highIndex = inOrderTraversal.index(high)
        output = 0

        for i in range(lowIndex, highIndex + 1):
            output += inOrderTraversal[i]

        return output

    def inorder(self, root, inOrderTraversal):
        if root:
            self.inorder(root.left, inOrderTraversal)

            inOrderTraversal.append(root.val)

            self.inorder(root.right, inOrderTraversal)
