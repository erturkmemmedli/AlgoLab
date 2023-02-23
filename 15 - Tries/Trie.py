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
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.isEnd


    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

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

    def search(self, word):
        node = self.root
        
        for char in word:
            if char not in node.children:
                return False
        
            node = node.children[char]
        
        return node.endOfString

    def startsWith(self, prefix):
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return False
        
            node = node.children[char]
        
        return True
