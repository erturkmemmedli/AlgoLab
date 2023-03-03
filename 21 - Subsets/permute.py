from collections import deque

class Solution:
    def permute(self, nums):
        result = []
        permutations = deque([[]])
        for num in nums:
            for _ in range(len(permutations)):
                permutation = permutations.popleft()
                for i in range(len(permutation) + 1):
                    subset = permutation[:]
                    subset.insert(i, num)
                    if len(subset) == len(nums):
                        result.append(subset)
                    else:
                        permutations.append(subset)
        return sorted(result)
        
# Alternative solution

from collections import deque

class Solution(object):
    def permute(self, nums):
        numsLength = len(nums)
        result = []
        permutations = deque()
        
        permutations.append([])
        
        for currentNumber in nums:
            n = len(permutations)

            for _ in range(n):
                oldPermutation = permutations.popleft()
            
                for j in range(len(oldPermutation)+1):
                    newPermutation = list(oldPermutation)
                    newPermutation.insert(j, currentNumber)
            
                    if len(newPermutation) == numsLength:
                        result.append(newPermutation)
                    else:
                        permutations.append(newPermutation)

        return result
