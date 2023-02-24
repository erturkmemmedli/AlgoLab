class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

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
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    uf.union(i, j)
        
        for i in range(n):
            uf.parent[i] = uf.find(uf.parent[i])

        return len(set(uf.parent))
        
# Official solution

class UnionFind:
    def __init__(self, n):
        self.parent = [node for node in range(n)]

    def find(self, A):
        while A != self.parent[A]:
            A = self.parent[A]

        return A

    def union(self, A, B):
        rootA = self.find(A)
        rootB = self.find(B)

        if rootA == rootB:
            return 0

        self.parent[rootA] = rootB

        return 1


class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        unionFind = UnionFind(n)

        sum = 0

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    sum += unionFind.union(i, j)

        return n - sum
