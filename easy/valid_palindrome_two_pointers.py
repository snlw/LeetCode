# https://leetcode.com/problems/valid-palindrome/submissions/1276096499/

# Time Complexity: O(n)
# Space Complexity: O(1)

# Type: Two Pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Remove all punctuations and whitespaces 
        alphanumeric_string = [char for char in s if char.isalpha() or char.isdigit()]

        if (len(alphanumeric_string) == 0):
            return True

        left = 0
        right = len(alphanumeric_string) - 1

        while (left < right):
            # Check for incorrect match 
            if alphanumeric_string[left].lower() != alphanumeric_string[right].lower():
                return False
            else:
                left += 1
                right -= 1
        
        return True


        
