"""
https://leetcode.com/problems/number-of-substrings-with-only-1s/submissions/1325281028/

TC: O(n)
SC: O(1)
"""
class Solution:
    def numSub(self, s: str) -> int:
        """
        1 : 1
        11 : 2 + 1
        111 : 3 + 2 + 1
        1111 : 4 + 3 + 2 + 1
        11111 : 5 + 4 + 3 + 2 + 1
        111111 : 6 + 5 + 4 + 3 + 2 + 1
        """
        def getSubstringCount(n):
            if n % 2 == 0:
                return (n + 1)*(n // 2)
            if n % 2 == 1:
                return (n + 1)*(n // 2) + (n // 2) + 1
        
        ans = 0
        left = 0
        count = 0
        while left < len(s):
            if s[left] == "0":
                ans += getSubstringCount(count)
                count = 0
            elif s[left] == "1":
                count += 1
            
            left += 1
        if count > 0:
            ans += getSubstringCount(count)

        return ans % (10**9 + 7)

        
        
