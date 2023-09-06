from collections import deque

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        visits = [[0 for _ in range(m)] for _ in range(n)]
        visits[0][0] = 1
        visited = set()

        queue = deque([(0, 0)])
        while queue:
            x, y = queue.popleft()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for x1, y1 in [(x + 1, y), (x, y + 1)]:
                if x1 < n and y1 < m:
                    visits[x1][y1] += visits[x][y]
                    queue.append((x1, y1))
        
        return visits[-1][-1]
