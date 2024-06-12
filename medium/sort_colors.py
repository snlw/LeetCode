"""
https://leetcode.com/problems/sort-colors/submissions/1285515457

Time Complexity: O(n2)
Space Complexity: O(1)

Type: Bubble Sort
"""
class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(i, j, nums):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        n = len(nums)

        for i in range(n - 1):
            current = nums[i]
            minimum = min(nums[i + 1 :])
            if minimum < current:
                indexes = [j for j in range(i + 1, n) if nums[j] == minimum]
                swap(indexes[-1], i, nums)

        return nums
