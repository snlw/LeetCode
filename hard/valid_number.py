"""
https://leetcode.com/problems/valid-number/submissions/1331942581/
"""
class Solution:
    def isNumber(self, s: str) -> bool:
        def isInteger(s):
            ## String should only have 1 -/+ at index 0
            ## String should only contain digits
            for i in range(len(s)):
                char = s[i]
                if not char.isdigit():
                    if i == 0 and char in ["-", "+"]:
                        continue
                    else:
                        return False
            return True

        def isDecimal(s):
            ## String should contain "."
            if "." not in s:
                return False
            if s == ".":
                return False
            ## String should only contain 1 "."
            splitted = s.split(".")
            if len(splitted) != 2:
                return False
            front, back = splitted
            ## Case "+.", "-."
            if (front == "+" or front == "-") and back == "":
                return False
            return (isInteger(front) if front else True) and (back.isdigit() if back else True)
        
        def isExponential(s, delimiter):
            splitted = s.split(delimiter)
            if len(splitted) != 2:
                return False
            front, back = splitted
            if front == "" or front == "+" or front == "-" or back == "":
                return False
            if back == "+" or back == "-":
                return False
            return (isInteger(front) or isDecimal(front)) and isInteger(back)

        if "e" in s:
            if len(s) == 1:
                return False
            return isExponential(s, "e")
        elif "E" in s:
            if len(s) == 1:
                return False
            return isExponential(s, "E")
        else:
            if s == "+" or s == "-":
                return False
            return isInteger(s) or isDecimal(s)
