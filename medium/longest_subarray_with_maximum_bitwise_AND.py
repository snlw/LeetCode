"""
https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/submissions/1389285532/?envType=daily-question&envId=2024-09-14
"""
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = max(nums)

        ans = 0
        subarrayLength = 0

        for i in range(len(nums)):
            if nums[i] == mx:
                subarrayLength += 1
            else:
                subarrayLength = 0
            ans = max(ans, subarrayLength)
        return ans
