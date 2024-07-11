"""
https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/submissions/1317037064/?envType=daily-question&envId=2024-07-11

TC: O(n)
SC: O(n)

Type: Stack
"""
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for char in s:
            if char == ')':
                section = ""
                while stack:
                    prev = stack.pop()
                    if prev == "(":
                        break
                    else:
                        section += prev
                for char in section:
                    stack.append(char)
            else:
                stack.append(char)

        return "".join(stack)
