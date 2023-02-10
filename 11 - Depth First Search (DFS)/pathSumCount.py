# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root, targetSum):
        self.total = 0
        self.dfs(root, targetSum)
        return self.total

    def dfs(self, node, target):
        if not node:
            return {}
        leftDict = self.dfs(node.left, target)
        rightDict = self.dfs(node.right, target)
        if node.val == target:
            self.total += 1
        newDict = {node.val: 1}
        for num in leftDict.keys():
            newNum = num + node.val
            newDict[newNum] = newDict.get(newNum, 0) + leftDict[num]
            if newNum == target:
                self.total += leftDict[num]
        for num in rightDict.keys():
            newNum = num + node.val
            newDict[newNum] = newDict.get(newNum, 0) + rightDict[num]
            if newNum == target:
                self.total += rightDict[num]
        return newDict

# Official solution

class Solution:   
    def pathSum(self, root, targetSum):
        return self.dfs(root,targetSum, [])

    def dfs(self, root, target, path):
        if root == None:
            return 0
  
        path.append(root.val)

        i = len(path) - 1
        pathSum = 0
        pathCount = 0

        while i >= 0:
            pathSum += path[i]
            i -= 1

            if pathSum == target:
                pathCount += 1

        pathCount += self.dfs(root.left, target, path)
        pathCount += self.dfs(root.right, target, path)

        path.pop()

        return pathCount
