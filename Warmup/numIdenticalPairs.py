from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums):
        counter = Counter(nums)
        answer = 0
        for key, val in counter.items():
            if val > 1:
                answer += (val - 1) * val // 2
        return answer
		
# Official solution given

class Solution:
    def numIdenticalPairs(self, nums):
        repeat = {}
        num = 0
        for i in nums:
            if i in repeat:
                if repeat[i] == 1:
                    num += 1
                else:
                    num += repeat[i]
                repeat[i] += 1
            else:
                repeat[i] = 1
        return num

