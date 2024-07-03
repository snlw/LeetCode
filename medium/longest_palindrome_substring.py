"""
https://leetcode.com/problems/longest-palindromic-substring/submissions/1308366219/

Time Complexity: O(n2)
Space Complexity: O(1)

Type: Two Pointers
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ""

        def expand(i, odd = True):
            if odd:
                left, right = i, i
            else:
                left, right = i, i + 1
            while left >= 0 and right < n:
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    break
            return s[left + 1:right]
                
        for i in range(n):
            odd = expand(i, odd = True)
            even = expand(i, odd = False)

            if len(odd) > len(ans):
                ans = odd
            if len(even) > len(ans):
                ans = even
        
        return ans



        
