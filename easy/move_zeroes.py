"""
https://leetcode.com/problems/move-zeroes/submissions/1295679879

Time Complexity: O(n)
Space Complexity: O(1)

Type: Two Pointers
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # def move(idx):
        #     for i in range(idx, n - 1):
        #         nums[i], nums[i + 1] = nums[i + 1], nums[i]

        # for i in range(n - 1, -1, -1):
        #     if nums[i] == 0:
        #         move(i)

        left = 0

        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
        

                
        
