"""
https://leetcode.com/problems/count-and-say/submissions/1329623856/

TC: O(n)
SC: O(n)
"""
class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"
        if n == 1:
            return ans

        def RLE(s: str):
            result = ""
            left = 0
            curr = s[left]
            count = 0
            while left < len(s):
                if s[left] == curr:
                    count += 1
                else:
                    result += str(count) + curr
                    curr = s[left]
                    count = 1
                left += 1

            result += str(count) + str(curr)

            return result

        for _ in range(2, n + 1):
            ans = RLE(ans)

        return ans
