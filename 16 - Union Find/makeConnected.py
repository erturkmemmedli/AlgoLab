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
        
        if root_a == root_b:
            return
        
        self.parent[root_b] = root_a

class Solution:
    def makeConnected(self, n, connections):
        if len(connections) < n - 1:
            return -1
            
        uf = UnionFind(n)

        for a, b in connections:
            uf.union(a, b)
            
        for i in range(n):
            uf.parent[i] = uf.find(i)

        return len(set(uf.parent)) - 1
        
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
            return 1

        self.parent[rootA] = rootB
        return 0

class Solution(object):
    def makeConnected(self, n, connections):
        if len(connections) < n - 1:
            return -1

        unionFind = UnionFind(n)
        extraEdges = 0

        for connection in connections:
            A, B = connection[0], connection[1]
            extraEdges += unionFind.union(A, B)

        components = 0

        for i in range(n):
            if i == unionFind.parent[i]:
                components += 1

        if extraEdges >= components - 1:
            return components - 1

        return -1
