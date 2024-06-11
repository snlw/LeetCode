"""
https://leetcode.com/problems/combination-sum/submissions/1285018431/

Time Complexity: O(target)
Space Complexity: O(target)

Type: DP
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]

        for c in candidates:
            if c <= target:
                dp[c].append([c])

        for i in range(1, target + 1):
            if len(dp[i]) != 0:
                for combi in dp[i]:
                    for c in candidates:
                        total = sum(combi) + c
                        if total <= target:
                            newCombi = sorted(combi + [c])
                            if newCombi not in dp[total]:
                                dp[total].append(newCombi)

        return dp[target]
