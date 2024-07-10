"""
https://leetcode.com/problems/generate-parentheses/submissions/1316036567/

TC: O(4*n)
SC: O(n)

Type: Backtracking, Recursion, DFS
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(openParentheses, closeParentheses, s):
            if openParentheses == closeParentheses and openParentheses + closeParentheses == n * 2:
                ans.append(s)
                return
            
            if openParentheses < n:
                dfs(openParentheses + 1, closeParentheses, s + "(")
            
            if closeParentheses < openParentheses:
                dfs(openParentheses, closeParentheses + 1, s + ")")
            
        dfs(0, 0, "")

        return ans
