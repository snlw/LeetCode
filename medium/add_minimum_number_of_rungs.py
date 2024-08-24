"""
https://leetcode.com/problems/add-minimum-number-of-rungs/submissions/1366409868/

TC: O(n)
SC: O(1)
"""
class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        current = 0
        ans = 0

        for rung in rungs:
            diff = rung - current
            if diff > dist:
                ans += diff // dist
                if diff % dist == 0:
                    ans -= 1
            current = rung

        return ans
            
