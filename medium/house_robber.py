"""
https://leetcode.com/problems/house-robber/submissions/1313715657/

TC: O(n)
SC: O(n)

Type: DP
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] for _ in range(n)]

        dp[0] = nums[0]
        if n == 1:
            return dp[-1]
        
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]
