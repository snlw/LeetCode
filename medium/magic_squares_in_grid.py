"""
https://leetcode.com/problems/magic-squares-in-grid/submissions/1349453451/?envType=daily-question&envId=2024-08-09

TC: O(row x col)
SC: O(1)

"""
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagicSquare(row, col, g):
            check = [False] * 10
            for i in range(3):
                for j in range(3):
                    val = g[row + i][col + j]
                    if not 1 <= val <= 9 or check[val] == True:
                        return False
                    check[val] = True
            # Check if diagonal sums are the same
            diagonal1 = grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]
            diagonal2 = grid[row + 2][col] + grid[row + 1][col + 1] + grid[row][col + 2]

            if diagonal1 != diagonal2:
                return False

            # Check if all row sums are the same as the diagonal sums
            row1 = grid[row][col] + grid[row][col + 1] + grid[row][col + 2]
            row2 = grid[row + 1][col] + grid[row + 1][col + 1] + grid[row + 1][col + 2]
            row3 = grid[row + 2][col] + grid[row + 2][col + 1] + grid[row + 2][col + 2]

            if not (row1 == diagonal1 and row2 == diagonal1 and row3 == diagonal1):
                return False

            # Check if all column sums are the same as the diagonal sums
            col1 = grid[row][col] + grid[row + 1][col] + grid[row + 2][col]
            col2 = grid[row][col + 1] + grid[row + 1][col + 1] + grid[row + 2][col + 1]
            col3 = grid[row][col + 2] + grid[row + 1][col + 2] + grid[row + 2][col + 2]

            if not (col1 == diagonal1 and col2 == diagonal1 and col3 == diagonal1):
                return False
            return True

        ans = 0
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows - 2):
            for col in range(cols - 2):
                if isMagicSquare(row, col, grid):
                    ans += 1

        return ans
        
