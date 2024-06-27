"""
https://leetcode.com/problems/max-consecutive-ones-iii/submissions/1301697515/

Time Complexity: O(n)
Space Complexity: O(1)

Type: Sliding Window, Two Pointers
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)

        zeroes = 0

        left, right = 0, 0
        ans = -1

        while right < n:
            if nums[right] == 0:
                zeroes += 1

                while zeroes > k :
                    if nums[left] == 0:
                        zeroes -= 1
                    left += 1

            right += 1
            ans = max(ans, right - left)

        return ans
