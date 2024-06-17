"""
https://leetcode.com/problems/sum-of-square-numbers/submissions/1291276274

Time Complexity: O(n^0.5)
Space Complexity: O(1)

Type: Two Pointers
"""
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0 
        right = c ** 0.5 // 1

        while left <= right:
            total = left*left + right*right
            if total == c:
                return True
            elif total > c:
                right -= 1
            else:
                left += 1
        
        return False
        
