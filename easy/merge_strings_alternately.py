"""
https://leetcode.com/problems/merge-strings-alternately/submissions/1293603678

Time Complexity: O(n) 
Space Complexity: O(n + m)

Type: Strings
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""

        idx = 0
        while idx < len(word1) and idx < len(word2):
            merged += word1[idx]
            merged += word2[idx]
            idx += 1

        if idx < len(word2):
            merged += word2[idx:]
        elif idx < len(word1):
            merged += word1[idx:]
        
        return merged

        
