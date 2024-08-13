"""
https://leetcode.com/problems/combination-sum-ii/submissions/1353754379/?envType=daily-question&envId=2024-08-13

TC: O(n * 2^n)
SC: O(n * 2^n)

Type: Backtracking, Recusrion
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []
        combinations = []

        candidates.sort()

        def backtrack(index, targetSum):
            if targetSum == 0:
                ans.append(combinations[:])

            if index == n or targetSum <= 0:
                return

            for i in range(index, n):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                combinations.append(candidates[i])
                backtrack(i + 1, targetSum - candidates[i])
                combinations.pop()

        backtrack(0, target)
        return ans
