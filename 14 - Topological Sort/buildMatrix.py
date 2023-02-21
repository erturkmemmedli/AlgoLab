from collections import deque

class Solution:
    def buildMatrix(self, k, rowConditions, colConditions):
        # Both for rows and columns, Kahn's Algorithm will be applied separately.
        # Topologically sorted rows and columns will show the correct positions of numbers (1 to k) in matrix (k x k).

        rows = self.topologicalSort(k, rowConditions)
        cols = self.topologicalSort(k, colConditions)

        if rows == [] or cols == []:
            return []

        indices = {i: [] for i in range(1, k + 1)}

        for idx, row in enumerate(rows):
            indices[row].append(idx)

        for idx, col in enumerate(cols):
            indices[col].append(idx)

        matrix = [[0] * k for _ in range(k)]

        for num, [row, col] in indices.items():
            matrix[row][col] = num

        return matrix

    def topologicalSort(self, n, edges):
        graph = {i: [] for i in range(1, n + 1)}
        in_degree = {i: 0 for i in range(1, n + 1)}

        for start, end in edges:
            graph[start].append(end)
            in_degree[end] += 1

        queue = deque([node for node, degree in in_degree.items() if not degree])

        toposort = []

        while queue:
            node = queue.popleft()
            toposort.append(node)

            for neighbor in graph[node]:
                in_degree[neighbor] -= 1

                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return toposort if len(toposort) == n else []
        
# Official solution

from collections import deque
class Solution:
    def buildMatrix(self, k, R, C):
        answerwer1, answerwer2 = self.helper(k, R), self.helper(k, C)

        if not answerwer1 or not answerwer2:
            return []

        A = [[0] * k for _ in range(k)]
        
        for i in range(k):
            A[answerwer1.index(i)][answerwer2.index(i)] = i + 1

        return A

    def helper(self, k, A):
        nxt, indegree = [set() for _ in range(k)], [0] * k
        dq, answer = deque(), []
        A = set([tuple(a) for a in A])
        
        for i, j in A:
            nxt[i - 1].add(j - 1)
            indegree[j - 1] += 1

        for i in range(k):
            if indegree[i] == 0:
                dq.append(i)

        while dq:
            current = dq.popleft()
            answer.append(current)

            for cand in nxt[current]:
                indegree[cand] -= 1

                if indegree[cand] == 0:
                    dq.append(cand)

        return answer if len(answer) == k else []
