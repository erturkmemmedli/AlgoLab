class TrieNode:
    def __init__(self):
        self.children = [[] for _ in range(10)]
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def get_root(self):
        return self.root

    def insert(self, number):
        node = self.root

        for num in number:
            if node.children[int(num)] == []:
                node.children[int(num)] = TrieNode()

            node = node.children[int(num)]

class Solution:
    def lexicalOrder(self, n):
        trie = Trie()

        for i in range(1, n + 1):
            trie.insert(str(i))

        root = trie.get_root()
        current = 0
        self.output = []

        self.dfs(root, current)

        return self.output
        
    def dfs(self, node, current):
        for i in range(10):
            if node.children[i]:
                self.output.append(current + i)
                self.dfs(node.children[i], 10 * (current + i))
            elif i != 0:
                return
                
# Official solution

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, num):
        node = self.root

        for digit in str(num):
            if digit not in node.children:
                node.children[digit] = TrieNode()

            node = node.children[digit]

        node.endOfString = True
        

class Solution:
    def lexicalOrder(self, n):
        trie = Trie()

        for i in range(1, n+1):
            trie.insert(i)

        result = []

        self.dfs(trie.root, 0, result)
        answer = []

        for num in result:
            if num <= n:
                answer.append(num)

        return answer
    
    def dfs(self, node, num, res):
        if node.endOfString:
            res.append(num)

        for key in node.children:
            self.dfs(node.children[key], num * 10 + int(key), res)
