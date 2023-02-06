class Solution:
    def nextGreatestLetter(self, letters, target):
        left, right = 0, len(letters) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return letters[(right + 1) % len(letters)]
        
# Official solution

class Solution:
    def nextGreatestLetter(self, letters, target):
        start = 0
        end = len(letters) - 1

        if target < letters[start] or target >= letters[end]:
            return letters[start]

        while start <= end:
            middle = start + (end - start) // 2
            candidate = letters[middle]

            if target < candidate:
                end = middle - 1
            if target >= candidate:
                start = middle + 1

        return letters[start]
