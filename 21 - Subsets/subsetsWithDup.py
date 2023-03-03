class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        result = [[]]
        for i in range(len(nums)):
            start = 0
            if i > 0 and nums[i] == nums[i-1]:
                start = end + 1
            end = len(result) - 1
            for j in range(start, end + 1):
                subset = result[j][:]
                subset.append(nums[i])
                result.append(subset)
        return sorted(result)
        
# Official solution

class Solution:
    def subsetsWithDup(self, nums):
      nums.sort()

      subsets = []
      subsets.append([])
      
      startIndex, endIndex = 0, 0
      
      for i in range(len(nums)):
        startIndex = 0
      
        if i > 0 and nums[i] == nums[i - 1]:
          startIndex = endIndex + 1
      
        endIndex = len(subsets) - 1
      
        for j in range(startIndex, endIndex+1):
          set1 = list(subsets[j])
      
          set1.append(nums[i])
          subsets.append(set1)
      
      return subsets
