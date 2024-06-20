"""
https://leetcode.com/problems/magnetic-force-between-two-balls/submissions/1294677211

Time Complexity: O(nlog n + nlog ((position[n-1] - position[0]) / (m-1)))
Space Complexity: O(1)

Type: Binary Search
"""
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        minD = 1
        maxD = (position[-1] - position[0]) // (m - 1)

        ans = 1

        def good(p, d, m):
            count = 1
            placed = p[0]
            for i in range(1, len(p)):
                if p[i] - placed >= d:
                    count += 1
                    placed = p[i]
                if count >= m:
                    return True
            return False

        if good(position[:], maxD, m):
            return maxD

        while minD <= maxD:
            midD = minD + (maxD - minD) // 2
            if good(position[:], midD, m):
                ans = midD
                minD = midD + 1
            else:
                maxD = midD - 1

        return ans
