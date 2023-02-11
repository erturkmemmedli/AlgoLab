# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        queue = deque([root])
        depth = 0
        while queue:
            levelSize = len(queue)
            depth += 1
            for _ in range(levelSize):
                node = queue.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth
        
# Official solution

class Solution:
    def minDepth(self, root):
        if root == None:
            return 0

        queue = [root]
        minDepth = 0

        while queue:
            levelSize = len(queue)
            minDepth += 1

            for _ in range(levelSize):
                currentNode = queue.pop(0)

                if currentNode.left == None and currentNode.right == None:
                    return minDepth

                if currentNode.left:
                    queue.append(currentNode.left)

                if currentNode.right:
                    queue.append(currentNode.right)

        return minDepth
