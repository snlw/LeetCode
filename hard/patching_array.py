"""
https://leetcode.com/problems/patching-array/submissions/1290233729

Time Complexity: O(n)
Space Complexity: O(1)

Type: Greedy
"""
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        count = 0
        missed = 1
        i = 0

        while missed <= n:
            if i < len(nums) and nums[i] <= missed:
                missed += nums[i]
                i += 1
            else:
                missed += missed
                count += 1
        return count
            
