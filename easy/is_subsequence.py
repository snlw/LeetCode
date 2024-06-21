"""
https://leetcode.com/problems/is-subsequence/submissions/1295686413/

Time Complexity: O(len(t))
Space Complexity: O(1)

Type: Two Pointers
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0

        if len(s) == 0:
            return True

        for i in range(len(t)):
            if left >= len(s):
                return True

            if t[i] == s[left]:
                left += 1

        return left == len(s)
        
