"""
https://leetcode.com/problems/jump-game-ii/submissions/1340485838/

TC: O(n)
SC: O(n)

Type: DP
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10 ** 20
        dp = [INF] * n
        dp[0] = 0

        for i in range(n):
            if dp[i] == INF:
                continue
            for j in range(i, i + nums[i] + 1):
                if j >= n:
                    break
                dp[j] = min(dp[j], dp[i] + 1)

        return dp[-1]
        
