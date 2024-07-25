"""
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/submissions/1332617037/

TC: O(n)
SC: O(n)

Type: Stack
"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        openParentheses = 0
        for char in s:
            if char == "(":
                openParentheses += 1
            elif char == ")":
                if openParentheses > 0:
                    substring = char
                    while stack[-1] != "(":
                        last = stack.pop()
                        substring = last + substring
                    stack[-1] = stack[-1] + substring
                    openParentheses -= 1
                    continue
                else:
                    continue

            stack.append(char)
        ## Scenario: "))(("
        if all([char in [")", "("] for char in stack]):
            return ""
        ## Scenario: Extra open parentheses "(a(b(c)d)"
        if openParentheses > 0:
            return "".join([char for char in stack if char != "("])

        return "".join(stack)
        
