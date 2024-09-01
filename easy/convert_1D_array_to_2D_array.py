"""
https://leetcode.com/problems/convert-1d-array-into-2d-array/submissions/1375068016/?envType=daily-question&envId=2024-09-01

TC: O(n)
SC: O(m * n)
"""
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        elements = m * n
        if elements != len(original):
            return []
        
        ans = [ [-1] * n for _ in range(m)]

        for i in range(len(original)):
            r = i // n
            c = i % n
            ans[r][c] = original[i]
        
        return ans
