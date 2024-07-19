"""
https://leetcode.com/problems/roman-to-integer/submissions/1325915441/

TC: O(n)
SC: O(1)

"""
class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        ans = 0
        n = len(s)
        i = 0
        while i < n:
            processedDouble = False
            char = s[i]
            if i < n - 1:
                if char == "I":
                    if s[i + 1] == "V":
                        ans += 4
                        processedDouble = True
                    elif s[i + 1] == "X":
                        ans += 9
                        processedDouble = True
                elif char == "X":
                    if s[i + 1] == "L":
                        ans += 40
                        processedDouble = True
                    elif s[i + 1] == "C":
                        ans += 90
                        processedDouble = True
                elif char == "C":
                    if s[i + 1] == "D":
                        ans += 400
                        processedDouble = True
                    elif s[i + 1] == "M":
                        ans += 900
                        processedDouble = True
            if processedDouble:
                i += 1
            else:
                ans += mapping[char]

            i += 1

        return ans
        
