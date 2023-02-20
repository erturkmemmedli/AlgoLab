from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = {i : [] for i in range(numCourses)}
        in_degree = {i : 0 for i in range(numCourses)}
        
        for start, end in prerequisites:
            graph[end].append(start)
            in_degree[start] += 1
            
        queue = deque()
        
        for node, degree in in_degree.items():
            if degree == 0:
                queue.append(node)
        
        output = []
        
        while queue:
            node = queue.popleft()
            output.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return len(output) == numCourses
      
# Official solution

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}
        inDegree = {i: 0 for i in range(numCourses)}

        for prereq in prerequisites:
            parent, child = prereq[0], prereq[1]

            graph[parent].append(child)
            inDegree[child] += 1

        queue = []

        for key in inDegree:
            if inDegree[key] == 0:
                queue.append(key)

        finishedCourses = []

        while queue:
            node = queue.pop(0)
            finishedCourses.append(node)

            for neighbor in graph[node]:
                inDegree[neighbor] -= 1

                if inDegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(finishedCourses) == numCourses:
            return True
        else:
            return False
