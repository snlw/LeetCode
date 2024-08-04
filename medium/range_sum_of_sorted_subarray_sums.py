"""
https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/submissions/1343992780/?envType=daily-question&envId=2024-08-04

TC: O(n^2 log n)
SC: O(n^2)
"""
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        rSum = []
        for i in range(n):
            if i == n - 1:
                rSum.append(nums[i])
                break
            for j in range(i + 1, n + 1):
                rSum.append(sum(nums[i:j]))

        rSum.sort()

        return sum(rSum[left - 1:right]) % MOD
        
