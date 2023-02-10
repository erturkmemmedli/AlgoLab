# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root):
        self.inorderList = []
        self.inorderDFS(root)
        return self.inorderList
    
    def inorderDFS(self, node):
        if not node:
            return
        self.inorderDFS(node.left)
        self.inorderList.append(node.val)
        self.inorderDFS(node.right)
        
# Official solution

class Solution:
    def inorderTraversal(self, root):
        output = []

        self.inorder(root, output)

        return output

    def inorder(self, root, output):
        if root == None:
            return root

        self.inorder(root.left, output)

        output.append(root.val)

        self.inorder(root.right, output)
