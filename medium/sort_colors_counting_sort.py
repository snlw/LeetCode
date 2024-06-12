"""
https://leetcode.com/problems/sort-colors/submissions/1285518891

Time Complexity: O(n)
Space Complexity: O(1)

Type: Counting Sort
"""
class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        freq = [0] * 3
        for x in nums: 
            freq[x] += 1

        idx = 0

        for x in range(3):
            nums[idx : idx + freq[x]] = [x] * freq[x]
            idx += freq[x]
