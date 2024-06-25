"""
https://leetcode.com/problems/maximum-average-subarray-i/submissions/1299897624/?envType=study-plan-v2&envId=leetcode-75

Time Complexity: O(n)
Space Complexity: O(1)

Type: Sliding Window
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)

        ans = sum(nums[:k])
        window = sum(nums[:k])

        for i in range(k, n):
            window += nums[i] 
            window -= nums[i - k]

            ans = max(ans, window)

        return ans/k


        
