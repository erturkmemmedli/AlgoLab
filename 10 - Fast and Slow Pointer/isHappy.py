class Solution:
    def isHappy(self, n):
        fast = slow = n
        while fast != 1:
            fast = self.digitSquareSum(self.digitSquareSum(fast))
            if fast == 1:
                break
            slow = self.digitSquareSum(slow)
            if fast == slow:
                return False
        return True
            
    def digitSquareSum(self, n):
        res = 0
        while n:
            x = n % 10
            res += x ** 2
            n //= 10
        return res
        
# Official solution

class Solution:
    def isHappy(self, n):
        fast = n
        slow = n

        while True:
            slow = self.computeSum(slow)
            fast = self.computeSum(self.computeSum(fast))

            if fast == slow:
                break

        return slow == 1

    def computeSum(self, n):
        sumValue = 0

        while n > 0:
            digit = n % 10
            sumValue += digit * digit
            n = n // 10

        return sumValue
