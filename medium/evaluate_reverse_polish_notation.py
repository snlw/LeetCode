# https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/1278552688/

# Time Complexity: O(n)
# Space Complexity: O(n)

# Type: Stack
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.lstrip("-").isdigit():
                stack.append(token)
            else:
                # Case where token is an operator
                # L (operator) R
                right = int(stack.pop())
                left = int(stack.pop())

                if token is "+":
                    stack.append(left + right)
                elif token is "-":
                    stack.append(left - right)
                elif token is "*":
                    stack.append(left * right)
                elif token is "/":
                    stack.append(left / right)
        
        return int(stack[0])
        
