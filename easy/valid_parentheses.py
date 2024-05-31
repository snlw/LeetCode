# https://leetcode.com/problems/valid-parentheses/submissions/1273041744/

# Time Complexity: O(n)
# Space Complexity: O(n)

# Type: Stack

class Solution:
    def __init__(self):
        self.parentheses_map = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            # If character is an opening parentheses, I add it to the stack
            if s[i] in self.parentheses_map: 
                stack.append(s[i])
            else:
                # Closing parentheses while stack is empty
                if len(stack) == 0:
                    return False

                # If character is a closing parentheses
                matching_parentheses = stack.pop()
                # Check if the character closes the latest added opening parentheses
                if (self.parentheses_map[matching_parentheses] != s[i]):
                    return False

        return len(stack) == 0

            
        
