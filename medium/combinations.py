"""
https://leetcode.com/problems/combinations/submissions/1315850492/

TC: O(n * k)
SC: O(k)

Type: Backtracking, Recursion
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        combinations = []

        def backtrack(start):
            if len(combinations) == k:
                ans.append(combinations[:])
                return
            
            for num in range(start, n + 1):
                combinations.append(num)
                backtrack(num + 1)
                combinations.pop()
        backtrack(1)

        return ans
        
