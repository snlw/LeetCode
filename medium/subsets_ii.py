"""
https://leetcode.com/problems/subsets-ii/submissions/1315833518/

TC: O(n * 2*n)
SC: O(n * 2*n)

Type: Backtracking, DFS, Recursion
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        nums.sort()

        def dfs(idx, carry):
            if idx == n:
                return carry
            newCombinations = []
            for c in carry:
                combination = c + [nums[idx]]
                if combination not in carry:
                    newCombinations.append(combination)
            
            return dfs(idx + 1, carry + newCombinations)

        return dfs(1, [[], [nums[0]]])
        
