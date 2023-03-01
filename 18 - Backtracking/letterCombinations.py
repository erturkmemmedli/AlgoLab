class Solution:
    def letterCombinations(self, digits):
        if not digits: return []
        
        self.hashmap = {'2': ['a', 'b', 'c'],
                        '3': ['d', 'e', 'f'],
                        '4': ['g', 'h', 'i'],
                        '5': ['j', 'k', 'l'],
                        '6': ['m', 'n', 'o'],
                        '7': ['p', 'q', 'r', 's'],
                        '8': ['t', 'u', 'v'],
                        '9': ['w', 'x', 'y', 'z']}

        self.result = []
        self.backtrack(digits, "")
        return self.result

    def backtrack(self, digits, path):
        if not digits:
            self.result.append(path)
            return
        for letter in self.hashmap[digits[0]]:
            self.backtrack(digits[1:], path + letter)
            
# Official solution

class Solution:
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []

        digitsMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        result = []

        self.backtrack(0, [], result, digitsMap, digits)

        return result

    def backtrack(self, index, path, result, digitsMap, digits):
        if len(path) == len(digits):
            result.append("".join(path))

            return

        possibleLetters = digitsMap[digits[index]]

        for letter in possibleLetters:
            path.append(letter)

            self.backtrack(index + 1, path, result, digitsMap, digits)

            path.pop()
