# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def averageOfLevels(self, root):
        queue = deque([root])
        averages = []
        while queue:
            levelSize = len(queue)
            levelSum = 0
            for _ in range(levelSize):
                node = queue.popleft()
                levelSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            averages.append(levelSum / levelSize)
        return averages
      
# Official solution

class Solution:
    def averageOfLevels(self, root):
        queue = [root]
        output = []

        while queue:
            levelSize = len(queue)
            levelSum = 0

            for _ in range(levelSize):
                currentNode = queue.pop(0)
                levelSum += currentNode.val

                if currentNode.left:
                    queue.append(currentNode.left)

                if currentNode.right:
                    queue.append(currentNode.right)

            average = levelSum / levelSize
            output.append(average)

        return output
