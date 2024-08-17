"""
https://leetcode.com/problems/strictly-palindromic-number/submissions/1358407056/

Explanation:
- No number greater than 3 can be strictly palindromic because in at least one base, the number will not be a palindrome

Example for n > 4:
- Consider base n - 1, n = 11
- Consider base n - 2, n = 12
"""
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False
