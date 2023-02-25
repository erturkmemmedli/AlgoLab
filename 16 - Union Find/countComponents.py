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
        if root_a != root_b:
            self.parent[root_b] = root_a

class Solution:
    def countComponents(self, n, edges):
        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a, b)
        roots = 0
        for i in range(n):
            if i == uf.parent[i]:
                roots += 1
        return roots
        
# Official solution

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, A):
        if self.parent[A] != A:
            self.parent[A] = self.find(self.parent[A])

        return self.parent[A]

    def union(self, A, B):
        xset = self.find(A)
        yset = self.find(B)

        if xset == yset:
            return

        if self.rank[xset] > self.rank[yset]:
            self.parent[yset] = self.parent[xset]
        elif self.rank[xset] < self.rank[yset]:
            self.parent[xset] = self.parent[yset]
        else:
            self.parent[xset] = self.parent[yset]
            self.rank[yset] += 1
            
class Solution:
    def countComponents(self, n, edges):
        unionFind = UnionFind(n)

        for A, B in edges:
            unionFind.union(A, B)
        
        parent = set()

        for i in range(n):
            parent.add(unionFind.find(i))

        return len(parent)
