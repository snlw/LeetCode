"""
https://leetcode.com/problems/minimum-time-difference/submissions/1392131180/?envType=daily-question&envId=2024-09-16
"""
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)
        MAX = 24 * 60

        def convert_to_minutes(t: str):
            h, m = t.split(":")
            return int(h) * 60 + int(m)

        converted_timepoints = sorted([convert_to_minutes(t) for t in timePoints])

        ans = MAX
        for i in range(1, n):
            diff = converted_timepoints[i] - converted_timepoints[i - 1]
            if diff == 0:
                return 0
            ans = min(ans, min(diff, MAX - diff))

        lastDiff = converted_timepoints[-1] - converted_timepoints[0]
        ans = min(ans, min(lastDiff, MAX - lastDiff))

        return ans

