"""
https://leetcode.com/problems/container-with-most-water/submissions/1295712336

Time Complexity: O(n)
Space Complexity: O(1)

Type: Two Pointers
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height) - 1

        volume = 0

        while left < right:
            newVolume = min(height[left], height[right]) * (right - left)
            if newVolume > volume:
                volume = newVolume

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return volume


        
