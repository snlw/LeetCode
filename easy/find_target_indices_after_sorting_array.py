"""
https://leetcode.com/problems/find-target-indices-after-sorting-array/submissions/1363496260/

TC: O(n)
SC: O(1)
"""
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans = []
        nums.sort()

        for i,v in enumerate(nums):
            if v == target:
                ans.append(i)

        return ans
