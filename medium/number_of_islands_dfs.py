# https://leetcode.com/problems/number-of-islands/submissions/1281819995/

# Time Complexity: O(n*m)
# Space Complexity: O(1)

# Type: DFS, Recursion
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    self.markIslands(i, j, grid)

        return count 

    def markIslands(self, i: int, j: int, grid: List[List[str]]) -> None:
        if grid[i][j] == "0" or grid[i][j] == "2":
            return
        
        grid[i][j] = "2"

        # Check TOP
        if i > 0:
            self.markIslands(i - 1, j, grid)
        # Check BOTTOM
        if i < len(grid) - 1:
            self.markIslands(i + 1, j, grid)
        # Check LEFT
        if j > 0:
            self.markIslands(i, j - 1, grid)
        # Check RIGHT
        if j < len(grid[0]) - 1:
            self.markIslands(i, j + 1, grid)

