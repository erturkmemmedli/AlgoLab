class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        s = str(x)
        return s == s[::-1]
		
# Official solution given

class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False

        reverseNumber = 0
        number = x

        while number > 0:
            reverseNumber = reverseNumber * 10 + number % 10
            number = number // 10

        return x == reverseNumber