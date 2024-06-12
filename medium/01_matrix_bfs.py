"""
https://leetcode.com/problems/01-matrix/submissions/1285847753/

Time Complexity: O(m * n)
Space Complexity: O(1)

Type: BFS
"""
from collections import deque
class Solution:
    def updateMatrix(self, mat):
        m = len(mat)
        n = len(mat[0])

        dp = [[-1] * n for _ in range(m)]

        visited = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    visited.append((i, j))
                    dp[i][j] = 0

        while visited:
            i, j = visited.popleft()
            adjacents=[(i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)]
            for x, y in adjacents:
                if x < 0 or x >= m or y < 0 or y >= n or dp[x][y] != -1:
                    continue
                visited.append((x, y))
                dp[x][y] = dp[i][j] + 1

        return dp
