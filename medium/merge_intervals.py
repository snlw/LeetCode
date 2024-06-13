"""
https://leetcode.com/problems/merge-intervals/submissions/1286790179/

Time Complexity: O(n log n)
Space Complexity: O(n)

Type: Two Pointers, Sort
"""
class Solution:
    def merge(self, intervals):
        n = len(intervals)

        left = 0
        right = n - 1

        while left <= right:
            currentLower, currentUpper = intervals[left]
            merged = False
            for i in range(left + 1, right + 1):
                # Partial overlap of either upper bound or lower bound
                if (
                    intervals[i][0] <= currentUpper <= intervals[i][1]
                    or intervals[i][0] <= currentLower <= intervals[i][1]
                ):
                    intervals[left][0] = min(currentLower, intervals[i][0])
                    intervals[left][1] = max(currentUpper, intervals[i][1])
                    intervals.pop(i)
                    right -= 1
                    merged = True
                    break
                # Full overlap of both bounds i.e. [[1,4],[2,3]]
                elif intervals[i][0] > currentLower and intervals[i][1] < currentUpper:
                    intervals.pop(i)
                    right -= 1
                    merged = True
                    break

            if not merged:
                left += 1

        return intervals
