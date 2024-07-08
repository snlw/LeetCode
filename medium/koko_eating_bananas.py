"""
https://leetcode.com/problems/koko-eating-bananas/submissions/1314027699/

TC: O(log n)
SC: O(1)

Type: Binary Search
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)
            
            if hours > h:
                left = mid + 1
            else:
                right = mid

        return left
        
