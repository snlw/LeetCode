"""
https://leetcode.com/problems/find-triangular-sum-of-an-array/submissions/1357524258/

TC: O(n ^ 2)
SC: O(n)

Type: Recursion
"""
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        def getSum(nums):
            if len(nums) == 1:
                return nums[0]
            new = []
            for i in range(1, len(nums)):
                new.append((nums[i] + nums[i - 1]) % 10)
            
            return getSum(new)

        return getSum(nums)
