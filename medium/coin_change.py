"""
https://leetcode.com/problems/coin-change/submissions/1284979798/

Time Complexity: O(amount)
Space Complexity: O(amount)

Type: DP
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [0 for _ in range(amount + 1)]

        for coin in coins:
            if coin <= amount:
                dp[coin] = 1

        for i in range(1, amount + 1):
            if dp[i] > 0:
                for coin in coins:
                    if i + coin <= amount:
                        if dp[i + coin] == 0:
                            dp[i + coin] = dp[i] + 1
                        else:
                            dp[i + coin] = min(dp[i] + 1, dp[i + coin])

        return -1 if dp[amount] == 0 else dp[amount]
