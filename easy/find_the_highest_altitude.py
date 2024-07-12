"""
https://leetcode.com/problems/find-the-highest-altitude/submissions/1318627371/?envType=study-plan-v2&envId=leetcode-75

TC: O(n)
SC: O(n)

Type: Prefix Sum
"""
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)

        prefixSum = [0]

        for i in range(n):
            prefixSum.append(prefixSum[-1] + gain[i])

        return max(prefixSum)
