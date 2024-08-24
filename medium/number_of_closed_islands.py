"""
https://leetcode.com/problems/number-of-closed-islands/submissions/1366400899/

TC: O(R * C)
SC: O(1)

Type: DFS
"""
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        ans = 0

        def floodfill(r, c):
            if grid[r][c] == 0:
                grid[r][c] = 2
                if r == 0 or r == R - 1 or c == 0 or c == C - 1:
                    nonlocal isClosed
                    isClosed = False
            else:
                return

            if 0 <= r + 1 <= R - 1:
                floodfill(r + 1, c)
            if 0 <= r - 1 <= R - 1:
                floodfill(r - 1, c)
            if 0 <= c + 1 <= C - 1:
                floodfill(r, c + 1)
            if 0 <= c - 1 <= C - 1:
                floodfill(r, c - 1)

        for r in range(1, R - 1):
            for c in range(1, C - 1):
                cell = grid[r][c]
                if cell == 1 or cell == 2:
                    continue
                isClosed = True
                floodfill(r, c)
                if isClosed:
                    ans += 1
        return ans
