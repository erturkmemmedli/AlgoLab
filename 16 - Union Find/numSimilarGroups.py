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
    def numSimilarGroups(self, strs):
        n = len(strs)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if self.similar(strs[i], strs[j]):
                    uf.union(i, j)
                
        connected_components = 0

        for i in range(n):
            if i == uf.parent[i]:
                connected_components += 1
            
        return connected_components

    def similar(self, x, y):
        indices = []

        for i in range(len(x)):
            if x[i] != y[i]:
                indices.append(i)

            if len(indices) > 2:
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


    def union(self, A, B):
        rootA = self.find(A)
        rootB = self.find(B)

        if rootA == rootB:
            return 0

        self.parent[rootA] = rootB

        return 1


class Solution(object):
    def numSimilarGroups(self, strs):
        n = len(strs)
        unionFind = UnionFind(n)

        for i in range(n):
            for j in range(n):
                if i != j and self.isSimilar(strs[i], strs[j]):
                    unionFind.union(i, j)
        
        sum = 0

        for i in range(n):
            if i == unionFind.parent[i]:
                sum += 1
        
        return sum

    def isSimilar(self, str1, str2):
        count = 0

        for i in range(len(str1)):
            if str1[i] != str2[i]:
                count += 1

            if count > 2:
                return False

        return True
