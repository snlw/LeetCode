"""
https://leetcode.com/problems/spiral-matrix-iii/submissions/1348548364/?envType=daily-question&envId=2024-08-08

TC: O(n^2), where n = max(r, c)
SC: O(r * c)
"""
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = [[rStart, cStart]]
        total = rows * cols
        steps = 1
        east_south = [(0, 1), (1, 0)]
        west_north = [(0, -1), (-1, 0)]
        heading_east = True

        while len(ans) < total:
            direction = east_south if heading_east else west_north
            for dy, dx in direction:
                for _ in range(steps):
                    rStart += dy
                    cStart += dx
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        ans.append([rStart, cStart])
            heading_east = not heading_east
            steps += 1
            
        return ans
