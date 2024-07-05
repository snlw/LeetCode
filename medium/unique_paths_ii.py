"""
https://leetcode.com/problems/unique-paths-ii/submissions/1310627243/

Time Complexity: O(m x n)
Space Complexity: O(m x n)

Type: DP
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                    continue

                if row == 0 or col == 0:
                    if (row > 0 and dp[row - 1][col] == 0) or (col > 0 and dp[row][col - 1] == 0):
                        dp[row][col] = 0
                    else:
                        dp[row][col] = 1
                    continue
                
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[-1][-1]
        
