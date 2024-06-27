"""
https://leetcode.com/problems/trapping-rain-water/submissions/1302076590/

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        def waterAtPosition(i):
            elevation = height[i]
            left = max(height[:i])
            right = max(height[i+1:])
            water = min(left, right) - elevation
            return max(water, 0)

        trapped = 0
        for i in range(1, n - 1):
            trapped += waterAtPosition(i)

        return trapped
        
