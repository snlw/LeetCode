"""
https://leetcode.com/problems/basic-calculator-ii/submissions/1331595218/

TC: O(n)
SC: O(n)

Type: Stack
"""
class Solution:
    def calculate(self, s: str) -> int:
        ## Remove whitespaces
        s = s.replace(" ", "")
        groups = []

        ## [ "1", "+", "9", "/" "10"]
        for char in s:
            if char not in ['+', '-', '*', '/'] and groups and groups[-1].isdigit():
                groups[-1] += char
            else:
                groups.append(char)

        stack = []
        ptr = 0
        ## Evaluate priority for multiplication and division operations
        while ptr < len(groups):
            char = groups[ptr]
            if char in ["*", "/"]:
                p1 = stack.pop()
                p2 = groups[ptr + 1]
                if char == "*":
                    stack.append(int(p1) * int(p2))
                else:
                    stack.append(int(p1) / int(p2))
                ptr += 1
            else:
                stack.append(char)
            ptr += 1

        ## Evaluate remaining operations
        ans = int(stack[0])
        ptr2 = 1
        while ptr2 < len(stack):
            char = stack[ptr2]
            if char == "+":
                ans += int(stack[ptr2 + 1])
                ptr2 += 2
            elif char == "-":
                ans -= int(stack[ptr2 + 1])
                ptr2 += 2

        return floor(ans)
            
        



