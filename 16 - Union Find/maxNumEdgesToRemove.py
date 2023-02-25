class UnionFind:
    def find(self, parent, a):
        while a != parent[a]:
            a = parent[a]
        return a

    def union(self, parent, a, b):
        root_a = self.find(parent, a)
        root_b = self.find(parent, b)
        if root_a == root_b:
            return parent, False
        parent[root_b] = root_a
        return parent, True

class Solution:
    def maxNumEdgesToRemove(self, n, edges):
        uf = UnionFind()
        alice_edges = set()
        bob_edges = set()
        shared_edges = set()
        redundant_edges = 0

        for typ, a, b in edges:
            if typ == 1:
                alice_edges.add((a - 1, b - 1))
            elif typ == 2:
                bob_edges.add((a - 1, b - 1))
            else:
                if (a - 1, b - 1) in alice_edges:
                    alice_edges.remove((a - 1, b - 1))
                    redundant_edges += 1
                if (a - 1, b - 1) in bob_edges:
                    bob_edges.remove((a - 1, b - 1))
                    redundant_edges += 1
                shared_edges.add((a - 1, b - 1))

        shared_parent, redundant_edges = self.unification(uf, list(range(n)), shared_edges, redundant_edges)   
        alice_parent, redundant_edges = self.unification(uf, shared_parent[:], alice_edges, redundant_edges)
        bob_parent, redundant_edges = self.unification(uf, shared_parent[:], bob_edges, redundant_edges)

        return redundant_edges if self.connected(alice_parent) and self.connected(bob_parent) else -1

    def unification(self, uf, parent, edges, redundant):
        for a, b in edges:
            parent, condition = uf.union(parent, a, b)
            if not condition:
                redundant += 1
        return parent, redundant

    def connected(self, parent):
        roots = 0
        for i in range(len(parent)):
            if parent[i] == i:
                roots += 1
                if roots > 1:
                    return False
        return True

# Official solution

class UnionFind:
    def __init__(self, n):
        self.parent = [node for node in range(n)]
        self.components = n - 1

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
        self.components -= 1

        return 1

    def united(self):
        return self.components == 1


class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        edges = sorted(edges, key=lambda edge: edge[0], reverse=True)

        alice = UnionFind(n + 1)
        bob = UnionFind(n + 1)
        edgesAdded = 0

        for edge in edges:
            edgeType, node1, node2 = edge[0], edge[1], edge[2]

            if edgeType == 3:
                added = alice.union(node1, node2) + bob.union(node1, node2)

                if added > 0:
                    edgesAdded += 1
                    
            elif edgeType == 2:
                edgesAdded += bob.union(node1, node2)
            elif edgeType == 1:
                edgesAdded += alice.union(node1, node2)

        if alice.united() and bob.united():
            return len(edges) - edgesAdded
        else:
            return -1
