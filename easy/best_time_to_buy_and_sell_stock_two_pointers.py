# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1273161464/

# Time Complexity: O(n)
# Space Complexity: O(1)

# Type: Two Pointers

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0

        left_index = 0
        right_index = 1

        while right_index < len(prices):
            if prices[left_index] < prices[right_index]:
                answer = max(prices[right_index] - prices[left_index], answer)
            else:
                left_index = right_index
            
            right_index += 1

        return answer
        
