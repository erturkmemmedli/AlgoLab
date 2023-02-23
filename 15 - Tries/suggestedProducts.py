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
