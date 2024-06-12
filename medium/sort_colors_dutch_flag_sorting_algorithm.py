"""
https://leetcode.com/problems/sort-colors/submissions/1285524991

Time Complexity: O(n)
Space Complexity: O(1)

Type: Dutch Flag Sorting Algorithm
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

        ## Initialize pointers
        l = 0
        m = 0 
        r = n - 1

        while (m <= r):
            match nums[m]:
                # Red
                case 0:
                    swap(m, l, nums)
                    m += 1
                    l += 1
                # White
                case 1:
                    m += 1
                # Blue
                case 2:
                    swap(m, r, nums)
                    r -= 1

        return nums
