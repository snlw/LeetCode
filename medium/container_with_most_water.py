"""
https://leetcode.com/problems/container-with-most-water/submissions/1315345934/

TC: O(n)
SC: O(1)

Type: Two Pointers
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        ans = -1
        left = 0
        right = n - 1

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            ans = max(ans, h * w)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans
