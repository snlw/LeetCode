"""
https://leetcode.com/problems/masking-personal-information/submissions/1357473428/

TC: O(n), to retrieve all digits in mask_phone
SC: O(1)
"""
class Solution:
    def maskPII(self, s: str) -> str:
        def mask_email(s):
            s = s.lower()
            name, domain = s.split("@")
            return name[0] + "*" * 5 + name[-1] + "@" + domain
        
        def mask_phone(s):
            digits = [d for d in s if d.isdigit()]
            lastFour = "".join(digits[-4:])

            prefix = ""
            if len(digits) > 10:
                prefix += "+" + (len(digits) - 10) * "*" + "-"

            return prefix + "***-***-" + lastFour

        if "@" in s:
            return mask_email(s)
        else:
            return mask_phone(s)
