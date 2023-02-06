class Solution:
    def dietPlanPerformance(self, calories, k, lower, upper):
        calory = sum(calories[:k])
        point = 1 if calory > upper else -1 if calory < lower else 0
        for i in range(len(calories) - k):
            calory += calories[i + k] - calories[i]
            if calory > upper:
                point += 1
            elif calory < lower:
                point -= 1
        return point
      
# Official solution

class Solution:
    def dietPlanPerformance(self, calories, k, lower, upper):
        windowSum = sum(calories[:k])
        points = 0

        if windowSum < lower:
            points -= 1
        if windowSum > upper:
            points += 1

        for i in range(len(calories) - k):
            windowSum = windowSum - calories[i] + calories[i + k]
            if windowSum < lower:
                points -= 1
            if windowSum > upper:
                points += 1

        return points
