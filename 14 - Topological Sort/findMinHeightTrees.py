from collections import deque

class Solution:
    def findMinHeightTrees(self, n, edges):
        if n <= 2:
            return list(range(n))

        graph = {i: [] for i in range(n)}
        in_degree = {i: 0 for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            in_degree[a] += 1
            in_degree[b] += 1
        
        queue = deque([key for key, val in in_degree.items() if val == 1])

        MHT = []

        while queue:
            level_length = len(queue)
            
            for _ in range(level_length):
                node = queue.popleft()
                in_degree[node] -= 1

                for neighbor in graph[node]:
                    if in_degree[neighbor] == 0:
                        continue

                    in_degree[neighbor] -= 1

                    if in_degree[neighbor] == 1:
                        queue.append(neighbor)

            if queue:
                MHT = sorted(list(queue), reverse = True)
            
        return MHT
        
# Official solution

class Solution:
    def findMinHeightTrees(self, n, edges):

        if n <= 2:
            return [i for i in range(n)]

        neighbors = [set() for i in range(n)]

        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)

        leaves = []

        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)

        remainingNodes = n

        while remainingNodes > 2:
            remainingNodes -= len(leaves)
            newLeaves = []

            while leaves:
                leaf = leaves.pop()
                neighbor = neighbors[leaf].pop()
                neighbors[neighbor].remove(leaf)

                if len(neighbors[neighbor]) == 1:
                    newLeaves.append(neighbor)

            leaves = newLeaves

        return leaves
