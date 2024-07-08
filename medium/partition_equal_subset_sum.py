"""
https://leetcode.com/problems/partition-equal-subset-sum/submissions/1314099428/

TC: O(n^2)
SC: O(n)

Type: DP
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)

        if total % 2 == 1:
            return False

        dp = set()
        dp.add(0)
        target = total // 2

        for i in range(n - 1, -1, -1):
            copy = set()
            for s in dp:
                new = s + nums[i]
                if new == target:
                    return True
                copy.add(new)
            dp.update(copy)

        return False
