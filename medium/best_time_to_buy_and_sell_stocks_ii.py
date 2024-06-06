# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/1279669756/
# Time complexity: O(N)
# Space complexity: O(1)

# Type: Arrays
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        profit = 0
        start = prices[0]

        for i in range(0, n):
            if start < prices[i]:
                profit += prices[i] - start
            start = prices[i]

        return profit

        
