"""
https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/submissions/1338123402/?envType=daily-question&envId=2024-07-30

TC: O(n)
SC: O(1)

Type: DP
"""
class Solution:
    def minimumDeletions(self, s: str) -> int:
        ## Find number of a's from index 1 to end
        aAfter = len([char for char in [*s][1:] if char == 'a'])
        bBefore = 0

        ans = float('inf')
        n = len(s)

        for i in range(n):
            if i != 0:
                prev = s[i - 1]
                curr = s[i]
                if prev == 'b':
                    bBefore += 1
                if curr == 'a':
                    aAfter -= 1

            ans = min(ans, aAfter + bBefore)
        return ans


        
