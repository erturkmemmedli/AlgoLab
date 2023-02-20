from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}
        in_degree = {i: 0 for i in range(numCourses)}
        
        for course, preq_course in prerequisites:
            graph[preq_course].append(course)
            in_degree[course] += 1
            
        queue = deque()
        
        for course, preq_count in in_degree.items():
            if preq_count == 0:
                queue.append(course)
                
        topologically_sorted_courses = []
        
        while queue:
            node = queue.popleft()
            topologically_sorted_courses.append(node)
            
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return topologically_sorted_courses if len(topologically_sorted_courses) == numCourses else []
        
# Official solution

class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}
        inDegree = {i: 0 for i in range(numCourses)}

        for prereq in prerequisites:
            parent, child = prereq[1], prereq[0]

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
            return finishedCourses
        else:
            return []
