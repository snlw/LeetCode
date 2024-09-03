"""
https://leetcode.com/problems/sum-of-digits-of-string-after-convert/submissions/1377186613/?envType=daily-question&envId=2024-09-03
"""
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def convertStringToDigits(s: str):
            return "".join([str(ord(char) - ord('a') + 1) for char in s])
        
        base = convertStringToDigits(s)

        def transform(s: str):
            result = 0
            for digit in s:
                result += int(digit)
            return result
        
        ans = int(base)
        while k:
            ans = transform(str(ans))
            k -= 1
        
        return ans
