"""
https://leetcode.com/problems/decode-string/submissions/1321596558/?envType=study-plan-v2&envId=leetcode-75

TC: O(n)
SC: O(n)

Type: Stack
"""
class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        stack = []
        
        for i in range(n):
            if s[i] == "]":
                substring = []
                while stack[-1] != "[":
                    substring.append(stack.pop())
                
                ## Remove Open Parentheses
                stack.pop()
                ## Get counter for substring
                counter = ""
                while stack and stack[-1].isdigit():
                    counter += stack.pop()
                counter = counter[::-1]

                ## Reverse substring 
                substring = substring[::-1]

                for _ in range(int(counter)):
                    stack.extend(substring)
                
                continue

            stack.append(s[i])
        
        return "".join(stack)
