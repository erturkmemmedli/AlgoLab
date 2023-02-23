class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

    def search(self, word):
        node = self.root
        for i, char in enumerate(word):
            if char not in node.children:
                return word
            node = node.children[char]
            if node.isEnd:
                return word[:i+1]
        return word
        

class Solution:
    def replaceWords(self, dictionary, sentence):
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        candidate_words = sentence.split()
        output = []
        for word in candidate_words:
            output.append(trie.search(word))
        return " ".join(output)
      
# Official solution

class TrieNode:
    def __init__(self):
        self.endOfString = False
        self.children = {}
        
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

    def replace(self, word):
        node = self.root

        for index, char in enumerate(word):
            if char not in node.children:
                return word

            node = node.children[char]

            if node.endOfString:
                return word[:index+1]

        return word     

class Solution:        
    def replaceWords(self, dictionary, sentence):
            trie = Trie()

            for root in dictionary:
                trie.insert(root)

            words = sentence.split()

            for i in range(len(words)):
                words[i] = trie.replace(words[i])

            return " ".join(words)
