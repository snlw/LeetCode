"""
https://leetcode.com/problems/grumpy-bookstore-owner/submissions/1295367525

Time Complexity: O(n2)
Space Complexity: O(n)

Type: Sliding Window
"""
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)

        notSatisfied = [customers[i] * grumpy[i] for i in range(n)]
        
        extra = 0
        idx = 0
        for i in range(n - minutes + 1):
            period = notSatisfied[i:i+minutes]
            if sum(period) > extra:
                extra = sum(period)
                idx = i

        for i in range(idx, idx + minutes):
            grumpy[i] = 0
        
        ans = 0
        for i in range(n):
            if grumpy[i] == 0:
                ans += customers[i]

        return ans

        
