class Solution:
    def intervalIntersection(self, firstList, secondList):
        resultList, i, j = [], 0, 0
        while i < len(firstList) and j < len(secondList):
            if firstList[i][1] < secondList[j][0]:
                i += 1
            elif secondList[j][1] < firstList[i][0]:
                j += 1
            else:
                start = max(firstList[i][0], secondList[j][0])
                end = min(firstList[i][1], secondList[j][1])
                resultList.append([start, end])
                if firstList[i][1] < secondList[j][1]:
                    secondList[j][0] = firstList[i][1]
                    i += 1
                else:
                    firstList[i][0] = secondList[j][1]
                    j += 1
        return resultList
      
# Official solution

class Solution:
    def intervalIntersection(self, firstList, secondList):
        i = 0
        j = 0
        result = []

        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            
            if start <= end:
                result.append([start, end])

            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return result
