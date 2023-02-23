class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for i, char in enumerate(word):
            if node.isEnd:
                return word[:i]
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

    def prefix(self, word, answer):
        node = self.root
        for i, char in enumerate(word):
            if node.isEnd:
                return word[:i]
            if char not in node.children:
                node.isEnd = True
                return word[:i]
            node = node.children[char]
        node.isEnd = True
        return word 

class Solution:
    def longestCommonPrefix(self, strs):
        trie = Trie()
        trie.insert(strs[0])
        answer = strs[0]
        for i in range(1, len(strs)):
            answer = trie.prefix(strs[i], answer)
        return answer
        
# Official solution

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.endOfString = True
    
    def findCommonPrefix(self):
        prefix = []
        node = self.root

        while len(node.children) == 1 and not node.endOfString:
            char = list(node.children.keys())[0]

            prefix.append(char)

            node = node.children[char]

        return "".join(prefix)

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        trie = Trie()

        for word in strs:
            trie.insert(word)
        
        return trie.findCommonPrefix()
