'''
Graph Valid Tree

You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that 
there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

Example 1:

Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true

Example 2:

Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false

Constraints:

1 <= n <= 2000
0 <= edges.length <= 5000
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no self-loops or repeated edges.
'''

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
