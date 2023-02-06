class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        windowSum = sum(arr[:k])
        count = 1 if windowSum / k >= threshold else 0
        for i in range(len(arr) - k):
            windowSum += arr[i + k] - arr[i]
            if windowSum / k >= threshold:
                count += 1
        return count
      
# Official solution

class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        count = 0
        windowSum = sum(arr[:k])

        if windowSum / k >= threshold:
            count += 1

        for i in range(len(arr) - k):
            windowSum = windowSum - arr[i] + arr[i + k]
            average = windowSum / k
            if average >= threshold:
                count += 1

        return count
