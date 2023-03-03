class Solution:
    def generateParenthesis(self, n):
        if n == 0:
            return [""]

        result = []

        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n - i - 1):
                    result.append("(" + left + ")" + right)

        return result
        
# Official solution

class Solution():
    def generateParenthesis(self, N):
        if N == 0:
            return [""]

        answer = []

        for c in range(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N - 1 - c):
                    answer.append("({}){}".format(left, right))

        return answer
