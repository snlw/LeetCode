"""
https://leetcode.com/problems/find-the-winner-of-the-circular-game/submissions/1313678987/?envType=daily-question&envId=2024-07-08

TC : O(n)
SC : O(1)

Type: Josephus Problem, Recursion
"""
class Solution:
        def findTheWinner(self, n: int, k: int) -> int:
            ans = 0

            for i in range(2, n + 1):
                ans = (ans + k) % i
                print(ans)
            
            return ans + 1
