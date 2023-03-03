from collections import deque

class Solution:
    def letterCasePermutation(self, s):
        result = []
        combinations = deque([""])

        for char in s:
            for _ in range(len(combinations)):
                string = combinations.popleft()

                if char.isdigit():
                    new_string = string + char

                    if len(new_string) == len(s):
                        result.append(new_string)
                    else:
                        combinations.append(new_string)

                else:
                    new_string1 = string + char.lower()
                    new_string2 = string + char.upper()

                    if len(new_string1) == len(s):
                        result.append(new_string1)
                        result.append(new_string2)
                    else:
                        combinations.append(new_string1)
                        combinations.append(new_string2)

        return sorted(result, key = lambda x: [x[i] for i in range(len(result) - 1, -1, -1)])
        
# Odfficial solution

class Solution():
    def letterCasePermutation(self, S):
        B = sum(letter.isalpha() for letter in S)
        answer = []

        for bits in range(1 << B):
            b = 0
            word = []

            for letter in S:
                if letter.isalpha():
                    if (bits >> b) & 1:
                        word.append(letter.lower())
                    else:
                        word.append(letter.upper())

                    b += 1
                else:
                    word.append(letter)

            answer.append("".join(word))

        return answer
