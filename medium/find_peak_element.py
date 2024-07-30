"""
https://leetcode.com/problems/find-peak-element/submissions/1338195682/

TC: O(log n)
SC: O(1)

Type: Binary Search
"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        # O(n) solution
        # for i in range(1, n - 2):
        #     if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
        #         return i

        # O(log n) solution
        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid + 1] > nums[mid]:
                left = mid + 1
            else:
                right = mid
        
        return left
        
