"""
https://leetcode.com/problems/minimum-increment-to-make-array-unique/submissions/1288238137/

Time Complexity: O(n)
Space Complexity: O(1)

Type: Sort, Arrays
"""
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        n = len(nums)

        nums.sort()

        count = 0 

        prev = nums[0]

        for i in range(1, n):
            if nums[i] <= prev:
                count += prev + 1 - nums[i]
                nums[i] = prev + 1
            
            prev = nums[i]

        return count
