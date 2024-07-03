"""
https://leetcode.com/problems/string-to-integer-atoi/submissions/1307982721/

Time Complexity: O(n)
Space Complexity: O(1)

Type: String
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        ## Remove leading whitespaces
        s = s.strip()

        if len(s) == 0:
            return 0

        ## Check for negative sign
        isNegative = False
        if s[0] == "-":
            isNegative = True
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]

        ## Find end of integer
        end = 0

        while end < len(s):
            if not s[end].isdigit():
                break
            end += 1

        start = 0

        while start < end:
            if s[start] == "0":
                start += 1
            else:
                break

        if start == end:
            return 0

        read = int(s[start:end])

        if isNegative:
            read *= -1

        ## Round integer
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if INT_MIN <= read <= INT_MAX:
            return read
        elif read < INT_MIN:
            return INT_MIN
        else:
            return INT_MAX
