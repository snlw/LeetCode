"""
https://leetcode.com/problems/ugly-number/submissions/1360353597/

TC: O(log n)
SC: O(log n) due to recursive call stack
"""
class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        
        def divide(num, divisor):
            while num % divisor == 0:
                num /= divisor
            return num
        
        for divisor in [5, 3, 2]:
            n = divide(n, divisor)
        
        return n == 1
