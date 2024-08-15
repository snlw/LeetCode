"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1356313110/

TC: O(n)
SC: O(1)

Type: Two Pointers
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        idx = 1

        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[idx] = nums[i]
                idx += 1
        return idx
