"""
https://leetcode.com/problems/unique-paths/submissions/1310607721/

Time Complexity: O(m x n)
Space Complexity: O(m x n)

Type: DP
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        
        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0:
                    dp[row][col] = 1
                    continue
                
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[-1][-1]
