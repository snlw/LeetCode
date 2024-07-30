"""
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/submissions/1338516864/

TC: O(n)
SC: O(n)

Type: Stack
"""
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if s == "":
            return 0

        stack = []
        for par in s:
            if par == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                    continue

            stack.append(par)
        return len(stack)

        
