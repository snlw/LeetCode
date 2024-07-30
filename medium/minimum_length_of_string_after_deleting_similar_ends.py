"""
https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/submissions/1338156559/?envType=daily-question&envId=2024-07-30

TC: O(n)
SC: O(1)

Type: Two Pointers, Recursion
"""
class Solution:
    def minimumLength(self, s: str) -> int:
        def deleteEnds(s: str, left:int, right: int):
            if left >= right or s[left] != s[right]:
                return right - left + 1
            else:
                char = s[left]

            while left <= right and s[left] == char:
                left += 1
            
            while right > left and s[right] == char:
                right -= 1
            
            return deleteEnds(s, left, right)

        return deleteEnds(s, 0, len(s) - 1)
