"""
https://leetcode.com/problems/delete-and-earn/submissions/1313774350/

TC : O(n log n)
SC : O(n)

Type: DP
"""
class Solution:
    def deleteAndEarn(self, nums) -> int:
        unique = sorted(set(nums))

        ## Generate a Hash Table for points
        table = dict()
        for num in nums:
            if num in table:
                table[num] += num
            else:
                table[num] = num

        dp = [[0] for _ in range(len(unique))]
        dp[0] = table[unique[0]]

        if len(unique) == 1:
            return dp[-1]

        dp[1] = max(dp[0], table[unique[1]]) if unique[1] - unique[0] == 1 else dp[0] + table[unique[1]]

        for i in range(2, len(unique)):
            if unique[i] - unique[i - 1] == 1:
                dp[i] = max(dp[i - 1], dp[i - 2] + table[unique[i]])
            else:
                dp[i] = dp[i - 1] + table[unique[i]]

        return dp[-1]
        
