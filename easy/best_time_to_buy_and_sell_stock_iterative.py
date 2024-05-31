# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1273165064/

# Time Complexity: O(n)
# Space Complexity: O(1)

# Type: Iterative

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0

        buy_price = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < buy_price:
                buy_price = prices[i]
            elif prices[i] - buy_price > answer:
                answer = prices[i] - buy_price

        return answer
        
