from collections import deque

class Solution:
    def getAncestors(self, n, edges):
        graph = {i:[] for i in range(n)}
        in_degree = {i:0 for i in range(n)}

        for start, end in edges:
            graph[start].append(end)
            in_degree[end] += 1

        queue = deque([node for node, degree in in_degree.items() if not degree])
        answer = [set() for _ in range(n)]

        while queue:
            node = queue.popleft()
            
            for neighbor in graph[node]:
                answer[neighbor].add(node)
                
                for element in answer[node]:
                    answer[neighbor].add(element)

                in_degree[neighbor] -= 1

                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return [sorted(list(ans)) for ans in answer]
        
# Official solution

from collections import defaultdict
class Solution:
    def getAncestors(self, n, edges):
        directChild = defaultdict(list)
        ans = [[] for _ in range(n)]

        for x, y in edges:
            directChild[x].append(y)

        for i in range(n):
            self.dfs(i, i, directChild, ans)
            
        return ans

    def dfs(self, x, curr, directChild, ans):
        for ch in directChild[curr]:
            if ans[ch] and ans[ch][-1] == x:
                continue

            ans[ch].append(x)
            
            self.dfs(x, ch, directChild, ans)
