"""
https://leetcode.com/problems/minimum-bit-flips-to-convert-number/submissions/1386181751/?envType=daily-question&envId=2024-09-11
"""
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = str(bin(start)[2:])
        goal = str(bin(goal)[2:])
        diff = len(start) - len(goal)
        if diff > 0:
            goal = '0' * diff + goal
        elif diff < 0:
            start = '0' * abs(diff) + start
        print(start, goal)
        ans = 0
        for i in range(len(start)):
            if start[i] != goal[i]:
                ans += 1
        return ans
