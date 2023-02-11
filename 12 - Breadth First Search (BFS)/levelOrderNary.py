"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        queue = deque([root])
        levelOrder = []
        while queue:
            levelSize = len(queue)
            level = []
            for _ in range(levelSize):
                currentNode = queue.popleft()
                level.append(currentNode.val)
                if not currentNode.children:
                    continue
                for node in currentNode.children:
                    queue.append(node)
            levelOrder.append(level)
        return levelOrder
        
# Official solution

class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        queue = [root]
        output = []

        while queue:
            levelTraversal = []
            levelSize = len(queue)

            for _ in range(levelSize):
                currentNode = queue.pop(0)

                levelTraversal.append(currentNode.val)

                if currentNode.children:
                    for child in currentNode.children:
                        queue.append(child)

            output.append(levelTraversal)

        return output
