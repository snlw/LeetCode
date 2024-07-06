"""
https://leetcode.com/problems/pass-the-pillow/submissions/1310991238/?envType=daily-question&envId=2024-07-06
"""
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        passes = time // (n - 1)
        rem = time % (n - 1)
        if passes % 2 == 0:
            return 1 + rem
        else:
            return n - rem
        
