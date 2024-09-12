"""
https://leetcode.com/problems/count-the-number-of-consistent-strings/submissions/1387626843/?envType=daily-question&envId=2024-09-12
"""
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        def isConsistent(word, allowed):
            result = True
            for char in word:
                if char not in allowed:
                    result = False
                    break
            return result

        for word in words:
            if isConsistent(word, allowed):
                ans += 1

        return ans
