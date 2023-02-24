class UnionFind:
    def __init__(self, n):
        self.parent = [node for node in range(n)]
        
    def find(self, node):
        while node != self.parent[node]:
            node = self.parent[node]
            
        return node
        
    def union(self, nodeA, nodeB):
        rootA = self.find(nodeA)
        rootB = self.find(nodeB)
        
        if rootA == rootB:
            return False
            
        self.parent[rootB] = rootA
        
        return True

class Solution:
    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False
            
        uf = UnionFind(n)
        
        for a, b in edges:
            if not uf.union(a, b):
                return False
        
        return True
        
# Official solution

class UnionFind:
    def __init__(self, n):
        self.parent = [node for node in range(n)]
        
    def find(self, A):
        while A != self.parent[A]:
            A = self.parent[A]

        return A
    
    def union(self, A,B):
        rootA = self.find(A)
        rootB = self.find(B)

        if rootA == rootB:
            return False

        self.parent[rootB] = rootA

        return True
        
class Solution:
    def validTree(self, n, edges):
        if len(edges) != n-1: 
            return False
        
        unionFind = UnionFind(n)
        
        for A,B in edges:
            if not unionFind.union(A,B):
                return False

        return True
