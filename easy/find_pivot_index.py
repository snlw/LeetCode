"""
https://leetcode.com/problems/find-pivot-index/submissions/1318684174/?envType=study-plan-v2&envId=leetcode-75

TC: O(n)
SC: O(1)

Type: Prefix Sum
"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        left = 0 
        right = sum(nums)

        for i in range(n):
            right -= nums[i]
            if right == left:
                return i
            left += nums[i]

        return -1
