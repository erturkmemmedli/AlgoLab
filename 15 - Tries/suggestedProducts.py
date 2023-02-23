class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def get_root(self):
        return self.root

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

            if len(node.suggestions) < 3:
                node.suggestions.append(word)

    def suggest(self, node, char):
        if node and char in node.children:
            return node.children[char], node.children[char].suggestions
            
        return None, []

class Solution:
    def suggestedProducts(self, products, searchWord):
        products.sort()
        trie = Trie()

        for product in products:
            trie.insert(product)

        output = []
        root = trie.get_root()

        for char in searchWord:
            if not root:
                output.append([])
            else:
                root, suggestion = trie.suggest(root, char)
                output.append(suggestion)

        return output

# Official solution

class TrieNode:
    def __init__(self):
        self.children = {}
        self.searchWords = []
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, data):
        node = self.root
        idx = 0

        for char in data:
            idx += 1

            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

            if len(node.searchWords) < 3:
                node.searchWords.append(data)
    
    def search(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return []

            node = node.children[char]

        return node.searchWords

class Solution:
    def suggestedProducts(self, products, searchWord):
        products.sort()
        trie = Trie()
        
        for product in products:
            trie.insert(product)
        
        result = []
        prefix = ""

        for char in searchWord:
            prefix += char
            result.append(trie.search(prefix))

        return result
