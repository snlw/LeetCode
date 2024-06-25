"""
https://leetcode.com/problems/increasing-triplet-subsequence/submissions/1295674174/

Time Complexity: O(n)
Space Complexity: O(1)

Type: Arrays
"""
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)

        left = 2**31
        mid = 2**31

        for i in range(n):
            if nums[i] < left:
                left = nums[i]

            if nums[i] > left and nums[i] < mid:
                mid = nums[i]

            if nums[i] > mid:
                return True

        return False
        
