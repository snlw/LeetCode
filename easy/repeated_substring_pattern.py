"""
https://leetcode.com/problems/repeated-substring-pattern/submissions/1334285235/

TC: O(1)
SC: O(1)
"""
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ## Concat 2 instances of s 
        ## i.e. "abab" --> "abababab"
        sDouble = s + s

        return s in sDouble[1:-1]
        
