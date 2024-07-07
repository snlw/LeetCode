t """
https://leetcode.com/problems/water-bottles/submissions/1312248931/?envType=daily-question&envId=2024-07-07
"""
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        empty = numBottles
        while empty >= numExchange:
            new = empty // numExchange 
            ans += new
            empty = empty % numExchange + new
        return ans
