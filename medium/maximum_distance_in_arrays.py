"""
https://leetcode.com/problems/maximum-distance-in-arrays/submissions/1357260713/

TC: O(log n)
SC: O(1)
"""
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        if len(arrays) == 2:
            return max(abs(arrays[0][0] - arrays[1][-1]), abs(arrays[0][-1] - arrays[1][0]))

        arraysWithLowest = sorted(arrays, key=lambda x:x[0])[:2]
        arraysWithHighest = sorted(arrays, key=lambda x:x[-1], reverse = True)[:2]

        ans = -1

        for arrL in arraysWithLowest:
            for arrH in arraysWithHighest:
                if arrL == arrH:
                    continue
                maxD = abs(arrL[0] - arrH[-1])
                ans = max(ans, maxD)

        return ans
