# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []
        queue = deque([root])
        levelOrder = []
        while queue:
            levelSize = len(queue)
            level = []
            for _ in range(levelSize):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levelOrder.append(level)
        return levelOrder[::-1]
        
# Official solution

class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []

        queue = [root]
        output = []

        while queue:
            levelSize = len(queue)
            levelTraversal = []

            for _ in range(levelSize):
                currentNode = queue.pop(0)
                levelTraversal.append(currentNode.val)

                if currentNode.left:
                    queue.append(currentNode.left)

                if currentNode.right:
                    queue.append(currentNode.right)

            output.insert(0, levelTraversal)

        return output
