"""
https://leetcode.com/problems/excel-sheet-column-number/submissions/1323045102/

TC: O(n)
SC: O(n)
"""
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        def getUnicode(char):
            return ord(char) - ord('A') + 1

        n = len(columnTitle)
        ans = 0
        for i in range(n - 1, -1, -1):
            char = columnTitle[i]
            power = n - i - 1
            ans += getUnicode(char) * (26 ** power)
        
        return ans
        
        
