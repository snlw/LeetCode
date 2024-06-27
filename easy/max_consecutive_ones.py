"""
https://leetcode.com/problems/max-consecutive-ones/submissions/1301654365/

Time Complexity: O(n)
Space Complexity: O(1)

Type: Prefix Sum
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        sum = 0

        for i in range(n):
            if nums[i] == 1:
                sum += 1
            if nums[i] == 0:
                if i > 0:
                    nums[i - 1] = sum
                    sum = 0
            if i == n - 1 and nums[i] == 1:
                nums[i] = sum

        return max(nums)
        
