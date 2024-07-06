"""
https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/submissions/1311254244/

TC: O(n)
SC: O(1)

Type: Array, Logic
"""
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        total = sum(chalk)
        ans = -1 
        k = k % total
        for i in range(n):
            if k < chalk[i]:
                ans = i
                break

            k -= chalk[i]
        return ans
