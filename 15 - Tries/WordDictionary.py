class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

    def search(self, word):
        node = self.root
        return self.dfs(node, word)

    def dfs(self, node, word):
        if not word:
            return node.isEnd
            
        if node.isEnd and not node.children:
            return False
            
        if word[0] == '.':
            for child in node.children:
                if self.dfs(node.children[child], word[1:]):
                    return True
                    
        elif word[0] not in node.children:
            return False
            
        else:
            return self.dfs(node.children[word[0]], word[1:])

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# Official solution

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.endOfString = True

    def search(self, word: str) -> bool:
        node = self.root

        return self.dfs(node, word)

    def dfs(self, node, word):
        if not word:
            return node.endOfString

        if word[0] == ".":
            for childNode in node.children.values():
                if self.dfs(childNode, word[1:]):
                    return True
        else:
            childNode = node.children.get(word[0])

            if not childNode:
                return False

            return self.dfs(childNode, word[1:])
