# https://leetcode.com/problems/climbing-stairs/submissions/1277285145/

# Time Complexity: O(n)
# Space Complexity: O(1)

# Type: Fibonacci Sequence, Recursion
class Solution:
    def climbStairs(self, n: int) -> int:
        return self.fibonacci(n) if n > 2 else n

    def fibonacci(self , n: int, n1: int = 1, n2: int = 2, counter:int = 2):
        if n - counter == 1:
            return n1 + n2

        counter += 1

        return self.fibonacci(n, n2, n1 + n2, counter)

