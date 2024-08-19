"""
https://leetcode.com/problems/2-keys-keyboard/submissions/1360895727/?envType=daily-question&envId=2024-08-19

TC: O(n^2)
SC: O(n)

Type: DP, Prime Factorization [O(n)]
"""
class Solution:
    def minSteps(self, n: int) -> int:
        """
        # DP
        MAX = 1000

        dp = [MAX] * (n + 1)
        dp[1] = 0

        for i in range(2, n + 1):
            for j in range(1, i // 2 + 1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j)

        return dp[n]
        """

        ans = 0
        d = 2
        while n > 1:
            # If d is prime factor, keep dividing
            # n by d until is no longer divisible
            while n % d == 0:
                ans += d
                n //= d
            d += 1
        return ans
