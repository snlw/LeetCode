"""
https://leetcode.com/problems/number-of-senior-citizens/submissions/1340143619/?envType=daily-question&envId=2024-08-01

TC: O(n)
SC: O(1)
"""
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        def parseAge(s):
            return int(s[11:13])

        ans = 0
        for d in details:
            age = parseAge(d)
            if age > 60:
                ans += 1

        return ans
