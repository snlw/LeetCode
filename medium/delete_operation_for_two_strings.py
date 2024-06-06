# https://leetcode.com/problems/delete-operation-for-two-strings/submissions/1279347772/

# Time Complexity: O(m * n)
# Space Complexity: O(n)

# Type: Dynamic Programming
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)

        dp = [[0] * (l1 + 1) for _ in range(l2 + 1)]

        for i in range(1, l2+1):
            for j in range(1, l1+1):
                if word2[i - 1] == word1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return abs(l1 - dp[-1][-1]) + abs(l2 - dp[-1][-1])
        
