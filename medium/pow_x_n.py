"""
https://leetcode.com/problems/powx-n/submissions/1331497282/

TC: O(log n)
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            x = 1/x
            n *= -1
        
        if n % 2 == 1:
            ans = self.myPow(x, n - 1)
            return x * ans
        else:
            ans = self.myPow(x, n // 2)
            return ans * ans
