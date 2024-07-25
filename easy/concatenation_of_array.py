"""
https://leetcode.com/problems/concatenation-of-array/submissions/1332734364/
"""
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ## return nums * 2
        ## return nums.extend(nums)
        return nums + nums
