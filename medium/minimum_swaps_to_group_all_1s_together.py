"""
https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/submissions/1341376678/?envType=daily-question&envId=2024-08-02

TC: O(n)
SC: O(1)

Type: Sliding Window
"""
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        ones = len([x for x in nums if x == 1])
        zeros = len([x for x in nums[:ones] if x == 0])
        ans = n
        for i in range(n):
            if nums[(i + ones) % n] == 0:
                zeros += 1
            if nums[i] == 0:
                zeros -= 1
            ans = min(zeros, ans)
        return ans
        
