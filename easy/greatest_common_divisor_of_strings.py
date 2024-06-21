"""
https://leetcode.com/problems/greatest-common-divisor-of-strings/submissions/1295403758

Time Complexity: O(min length of str1 and str2)
Space Complexity: O(max length of str1 and str2)

Type: String
"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)
        maximumLength = min(len1, len2)

        for i in range(maximumLength, 0, -1):
            if len1 % i == 0 and len2 % i == 0:
                divisor = str1[:i]
                str1Divided = [c for c in str1.split(divisor) if c != ""]
                str2Divided = [c for c in str2.split(divisor) if c != ""]
                if len(str1Divided) == 0 and len(str2Divided) == 0:
                    return divisor

        return ""

        
