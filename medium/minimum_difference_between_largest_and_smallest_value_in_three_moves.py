"""
https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/submissions/1307950766/?envType=daily-question&envId=2024-07-03

Time Complexity: O(n)
Space Complexity: O(1)

Type: Sorting
"""
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        ## Number of Changes
        k = 3 

        if len(nums) <= k + 1:
            return 0
        
        nums.sort()

        ans = float("inf")
        
        """
        Example : [20,75,81,82,95] (sorted)
        k + 1 (4) possibilities
        1. [82,82,82,82,95] --- 13
        2. [81,81,81,82,82] --- 1
        3. [75,75,81,82,95] --- 20
        4. [20,75,75,75,75] --- 55
        """
        for i in range(k + 1):
            diff = nums[i - k - 1] - nums[i]
            ans = min(diff, ans)

        return ans
