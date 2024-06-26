# https://leetcode.com/problems/first-bad-version/submissions/1277217550/

# Time Complexity: O(log n)
# Space Complexity: O(1)

# Type: Binary Search

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1

        left = 1
        right = n 

        while left < right:
            mid = (right + left) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

        
        
        
