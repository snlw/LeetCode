"""
https://leetcode.com/problems/find-missing-observations/submissions/1380005597/?envType=daily-question&envId=2024-09-05
"""
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total = mean * (m + n)
        totalN = total - sum(rolls)

        if totalN > n*6 or totalN < n:
            return []
        
        ans = [totalN // n] * n
        rem = totalN % n
        idx = 0
        while rem:
            if ans[idx] < 6:
                ans[idx] += 1
                rem -= 1
            else:
                idx += 1
        return ans
