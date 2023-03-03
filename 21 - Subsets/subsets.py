class Solution:
    def subsets(self, nums):
        result = [[]]
        for num in nums:
            for i in range(len(result)):
                subset = list(result[i])
                subset.append(num)
                result.append(subset)
        return sorted(result)
      
# Official solution

class Solution:
  def subsets(self, nums):
    subsets = []

    subsets.append([])

    for currentNumber in nums:
      n = len(subsets)
    
      for i in range(n):
        set1 = list(subsets[i])
    
        set1.append(currentNumber)
        subsets.append(set1)

    return subsets
