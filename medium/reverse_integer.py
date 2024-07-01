"""
https://leetcode.com/problems/reverse-integer/submissions/1306065658/

Time Complexity: O(n), n is the number of digits
Space Comeplxity: O(n), n is the number of digits

Type: String
"""
class Solution:
    def reverse(self, x: int) -> int:
        isNegative = True if x < 0 else False
        s = str(x*-1 if isNegative else x)
        ans = ""
        while s:
            digit = s[-1]
            ans += digit
            s = s[:-1]

        ans = -1 * int(ans) if isNegative else int(ans)

        if -2**31 <= ans <= 2**31 -1:
            return ans
        else:
            return 0

        


        
