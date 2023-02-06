from collections import deque

class Solution:
    def maxConsecutiveAnswers(self, answerKey, k):
        trueWindow = deque()
        falseWindow = deque()
        trueK = k
        falseK = k
        maxConfusion = 0
        for key in answerKey:
            trueWindow.append(key)
            falseWindow.append(key)
            if key == 'T':
                falseK -= 1
            else:
                trueK -= 1
            while falseK < 0:
                pop = falseWindow.popleft()
                if pop == 'T':
                    falseK += 1
                    break
            while trueK < 0:
                pop = trueWindow.popleft()
                if pop == 'F':
                    trueK += 1
                    break
            maxConfusion = max(maxConfusion, len(trueWindow), len(falseWindow))
        return maxConfusion
        
# Official solution

class Solution:
    def maxConsecutiveAnswers(self, answerKey, k):
        windowStart = 0
        windowEnd = 0
        tCount = 0
        fCount = 0
        maxLength = 0

        for windowEnd in range(len(answerKey)):
            if answerKey[windowEnd] == 'T':
                tCount += 1
            else:
                fCount += 1

            while tCount > k and fCount > k:
                if answerKey[windowStart] == 'T':
                    tCount -= 1
                else:
                    fCount -= 1

                windowStart += 1

            maxLength = max(maxLength, windowEnd - windowStart + 1)

        return maxLength
