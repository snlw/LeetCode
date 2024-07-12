"""
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/submissions/1318818767/?envType=study-plan-v2&envId=leetcode-75

TC: O(n)
SC: O(1)

Type: Sliding Window
"""
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = 0

        zeroCount = 0
        ans = 0

        if len(set(nums)) == 1 and list(set(nums))[0] == 1:
            return n - 1

        while right < n:
            if nums[right] == 0:
                zeroCount += 1

            while zeroCount > 1:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1

            maxOnes = right - left + 1 - zeroCount
            ans = max(ans, maxOnes)
            right += 1

        return ans
