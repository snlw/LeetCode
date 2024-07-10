"""
https://leetcode.com/problems/subsets/submissions/1315829007/

TC: O(n * 2^n)
SC: O(n * 2^n)

Type: DFS, Recursion, Backtracking
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def dfs(idx, new):
            if idx == n:
                return new
            newCombinations = []

            for a in new:
                newCombinations.append(a + [nums[idx]])

            return dfs(idx + 1, new + newCombinations)

        return dfs(1, [[], [nums[0]]])
        
