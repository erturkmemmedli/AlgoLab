class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        
    def find(self, a):
        while a != self.parent[a]:
            a = self.parent[a]

        return a

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        self.parent[root_b] = root_a

        return True

class Solution:
    def findRedundantConnection(self, edges):
        uf = UnionFind(len(edges))

        for a, b in edges:
            if not uf.union(a - 1, b - 1):
                return [a, b]
