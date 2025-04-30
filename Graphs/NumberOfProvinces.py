from collections import deque

class Solution:
    def findCircleNum(self, isConnected) -> int:
        n = len(isConnected)
        visited = set()
        res = 0

        def bfs(s):
            q = deque()
            q.append(s)
            visited.add(s)

            while q:
                s = q.popleft()
                for u in range(n):
                    if isConnected[s][u] == 1 and u not in visited:
                        visited.add(u)
                        q.append(u)

        for i in range(n):
            if i not in visited:
                bfs(i)
                res += 1
    
        return res