class Solution:
    def partition(self, s):
        self.result = []
        self.backtrack(s, [])
        return self.result

    def backtrack(self, string, path):
        if not string:
            self.result.append(path)
            return
        for i in range(len(string)):
            substring = string[:i+1]
            if substring == substring[::-1]:
                self.backtrack(string[i+1:], path + [substring])
                
# Official solution

class Solution:
    def partition(self, s):
        result = []
        self.backtrack(0, [], result, s)

        return result
        
        
    def isPalindrome(self, s):
        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] != s[end]:
                return False

            start += 1
            end -= 1

        return True


    def backtrack(self, start, path, result, s):
        if start == len(s):
            result.append(path[:])

            return

        for end in range(start, len(s)):
            if self.isPalindrome(s[start:end+1]):
                path.append(s[start : end + 1])

                self.backtrack(end+1, path, result, s)

                path.pop()
