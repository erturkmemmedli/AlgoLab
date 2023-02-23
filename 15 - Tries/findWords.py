class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.wordAwaiting = 0

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        self.wordAwaiting += 1
        node.isEnd = True

class Solution:
    def findWords(self, board, words):
        m, n = len(board), len(board[0])
        trie = Trie()
        node = trie.root
        result = []
        
        for word in words:
            trie.insert(word)

        for i in range(m):
            for j in range(n):
                char = board[i][j]
                if char in node.children:
                    self.dfs(trie, node.children[char], board, i, j, m, n, char, result)

        return result
            
    def dfs(self, trie, node, board, r, c, m, n, path, result):
        if not node or trie.wordAwaiting == 0:
            return

        if node.isEnd:
            result.append(path)
            node.isEnd = False
            trie.wordAwaiting -= 1

        temp = board[r][c]
        board[r][c] = "#"

        for row, col in [r-1, c], [r+1, c], [r, c-1], [r, c+1]:
            if m > row >= 0 <= col < n:
                char = board[row][col]
                if char in node.children:
                    self.dfs(trie, node.children[char], board, row, col, m, n, path + char, result)

        board[r][c] = temp
        
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
    
    def removeCharacters(self, word):
        node = self.root

        childList = []

        for char in word:
            childList.append([node, char])
            node = node.children[char]

        for pair in reversed(childList):
            parent = pair[0]
            childChar = pair[1]
            target = parent.children[childChar]

            if target.children:
                return

            del parent.children[childChar]

class Solution:
    def findWords(self, board, words):
        trie = Trie()
        result = []
        
        for word in words:
            trie.insert(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(trie, trie.root, board, i, j, result)
                
        return result

    def dfs(self, trie, node, board, row, col, result, word=''):
        if node.endOfString:
            result.append(word)
            node.endOfString = False
            trie.removeCharacters(word)

        if 0 <= row < len(board) and 0 <= col < len(board[0]):
            char = board[row][col]
            child = node.children.get(char)

            if child is not None:
                word += char
                board[row][col] = None

                for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    self.dfs(trie, child, board, row + rowOffset, col + colOffset, result, word)

                board[row][col] = char
