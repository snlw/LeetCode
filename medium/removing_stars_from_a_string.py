"""
https://leetcode.com/problems/removing-stars-from-a-string/submissions/1318386106/

TC: O(n)
SC: O(n)

Type: Stack
"""
class Solution:
    def removeStars(self, s: str) -> str:
        n = len(s)

        stack = []

        for i in range(n):
            if s[i] == '*':
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)

        
