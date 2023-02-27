'''
Number of Connected Components in an Undirected Graph

You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

Example 1:

Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Example 2:

Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1

Constraints:

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.
'''

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
