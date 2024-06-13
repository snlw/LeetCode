"""
https://leetcode.com/problems/rotting-oranges/submissions/1286751848/

Time Complexity: O(m * n)
Space Complexity: O(m * n)

Type: BFS
"""
from collections import deque

class Solution:
    def orangesRotting(self, grid):
        m = len(grid)
        n = len(grid[0])

        dp = [[-1] * n for _ in range(m)]

        visited = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    dp[i][j] = 0
                    visited.append((i, j))
        minutes = 0

        while visited:
            i, j = visited.popleft()
            adjacents = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for dx, dy in adjacents:
                if dx < 0 or dx >= m or dy < 0 or dy >= n or dp[dx][dy] != -1:
                    continue

                if grid[dx][dy] == 1:
                    dp[dx][dy] = dp[i][j] + 1
                    grid[dx][dy] = 2
                    visited.append((dx, dy))

                elif grid[dx][dy] == 2 or grid[dx][dy] == 0:
                    dp[dx][dy] = 0

                minutes = max(minutes, dp[dx][dy])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and dp[i][j] == -1:
                    return -1

        return minutes
