"""
https://leetcode.com/problems/missing-number/submissions/1355196671/

TC: O(n)
SC: O(1)

** sort() adds log n complexity
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = len(nums)

        for i in range(len(nums)):
            ans += i - nums[i]
        return ans
