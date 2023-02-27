'''
Alien Dictionary

There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. 
If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. 
If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.

Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:

Input: words = ["z","x"]
Output: "zx"

Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
 
Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.
'''

from collections import deque

class Solution:
    def alienOrder(self, words):        
        self.letters = set()
        
        for word in words:
            for letter in word:
                self.letters.add(letter)
        
        self.alienDictionary = {letter: set() for letter in self.letters}        
        self.inDegree = {letter: 0 for letter in self.letters}
        self.violation = False
        
        self.checkLetters(words)
        
        if self.violation:
            return ""
        
        queue = deque([node for node, degree in self.inDegree.items() if degree == 0])
        alienAlphabet = []
        
        while queue:
            node = queue.popleft()
            alienAlphabet.append(node)
            
            for neighbor in self.alienDictionary[node]:
                self.inDegree[neighbor] -= 1
                
                if self.inDegree[neighbor] == 0:
                    queue.append(neighbor)
                
        return "".join(alienAlphabet) if len(alienAlphabet) == len(self.letters) else ""

    def checkLetters(self, words):
        if not words:
            return
       
        if not words[0]:
            return self.checkLetters(words[1:])
         
        if any(word == "" for word in words):
            self.violation = True
            return
        
        check = [words[0]]
        
        for i in range(1, len(words)):            
            if words[i][0] == check[-1][0]:
                check.append(words[i])
                
            else:
                if len(check) > 1:
                    self.checkLetters([word[1:] for word in check])
                    
                    if self.violation:
                        return
                    
                self.alienDictionary[check[-1][0]].add(words[i][0])
                self.inDegree[words[i][0]] += 1
                check = [words[i]]
                
        if len(check) > 1:
            self.checkLetters([word[1:] for word in check])
            
# Official solution

from collections import deque
class Solution:
    def alienOrder(self, words):
        map = {}
        letters = [0 for i in range(26)]

        for i in range(len(words)):
            for j in range(len(words[i])):
                key = ord(words[i][j]) - ord("a")

                letters[key] = 0
                map[key] = set()

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            idx = 0

            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    key1 = ord(word1[j]) - ord("a")
                    key2 = ord(word2[j]) - ord("a")

                    count = letters[key2]

                    if key2 not in map[key1]:
                        letters[key2] = count + 1
                        map[key1].add(key2)

                    break
                elif j == min(len(word1), len(word2)) - 1 and len(word1) > len(word2):
                    return ""

        dictionary = deque()
        result = ""
        for i in range(26):
            if letters[i] == 0 and i in map:
                dictionary.appendleft(i)

        while len(dictionary) != 0:
            nextup = dictionary.pop()
            result += chr(nextup + ord("a"))
            greaterSet = map[nextup]
            
            for greater in greaterSet:
                letters[greater] -= 1
                
                if letters[greater] == 0:
                    dictionary.appendleft(greater)
                    
        if len(map) != len(result):
            return ""
            
        return result
