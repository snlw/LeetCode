"""
https://leetcode.com/problems/maximal-square/submissions/1328210369/

TC: O(m * n)
SC: O(m * n)

Type: DP
"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        ans = 0

        for i in range(cols):
            if matrix[0][i] == "1":
                dp[0][i] = 1
                ans = 1
        
        for j in range(rows):
            if matrix[j][0] == "1":
                dp[j][0] = 1
                ans = 1
 

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == "1":
                    dp[r][c] = min(min(dp[r - 1][c], dp[r - 1][c - 1]), dp[r][c - 1]) + 1
                    if dp[r][c] > ans:
                        ans = dp[r][c]

        return ans * ans
        
