'''
Walls and Gates
You are given an m x n grid rooms initialized with these three possible values.

-1  -> A wall or an obstacle.
0   -> A gate.
INF -> Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example 1:

Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

Example 2:

Input: rooms = [[-1]]
Output: [[-1]]
 
Constraints:

m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 2³¹ - 1.
'''

class Solution:
    def wallsAndGates(self, rooms):
        m = len(rooms)
        n = len(rooms[0])        
        gates = [] 
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    gates.append((i, j))
        for r, c in gates:
            for row, col in [r-1, c], [r, c-1], [r+1, c], [r, c+1]:
                self.dfs(rooms, m, n, row, col, 0, set())
            
    def dfs(self, rooms, m, n, row, col, distance, visited):
        if m > row >= 0 <= col < n and rooms[row][col] != -1 and rooms[row][col] != 0 and (row, col) not in visited:
            visited.add((row, col))
            rooms[row][col] = min(rooms[row][col], distance + 1)
            self.dfs(rooms, m, n, row - 1, col, rooms[row][col], visited)
            self.dfs(rooms, m, n, row + 1, col, rooms[row][col], visited)
            self.dfs(rooms, m, n, row, col - 1, rooms[row][col], visited)
            self.dfs(rooms, m, n, row, col + 1, rooms[row][col], visited)
            
# Official solution

class Solution:
    def wallsAndGates(self, rooms):
        MAX_ROW = len(rooms)
        MAX_COL = len(rooms[0])

        for i in range(MAX_ROW):
            for j in range(MAX_COL):
                if rooms[i][j] == 0:
                    self.bfs(i, j, MAX_ROW, MAX_COL, rooms)

        return rooms

    def bfs(self, row, col, MAX_ROW, MAX_COL, rooms):
        que = deque([(row + 1, col, 1), (row - 1, col, 1), 
                       (row, col + 1, 1), (row, col - 1, 1)])
        visited = set()

        while que:
            i, j, distance = que.popleft()

            if i < 0 or j < 0 or i >= MAX_ROW or j >= MAX_COL:
                continue
            if rooms[i][j] == 0 or rooms[i][j] == -1:
                continue
            if (i, j, distance) in visited:
                continue

            visited.add((i, j, distance))

            if distance < rooms[i][j]:
                rooms[i][j] = distance
                que.append((i + 1, j, distance + 1))
                que.append((i - 1, j, distance + 1))
                que.append((i, j + 1, distance + 1))
                que.append((i, j - 1, distance + 1))
