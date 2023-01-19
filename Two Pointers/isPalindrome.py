class Solution:
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            while not (s[left].isalpha() or s[left].isdigit()) and left < right:
                left += 1
            while not (s[right].isalpha() or s[right].isdigit()) and left < right:
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
        
# Official solution

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left <= right:
            while left < right and s[left].isalnum() == False:
                left += 1
            while left < right and s[right].isalnum() == False:
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True
