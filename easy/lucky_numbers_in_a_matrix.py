"""
https://leetcode.com/problems/lucky-numbers-in-a-matrix/submissions/1325760990/?envType=daily-question&envId=2024-07-19

TC: O(m * n)
SC: O(1)
"""
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ans = []
        rows = len(matrix)
        cols = len(matrix[0])

        minimumInRows = [min(matrix[row]) for row in range(rows)]
        maximumInColumns = [max(matrix[row][col] for row in range(rows)) for col in range(cols)]

        for row in range(rows):
            for col in range(cols):
                cell = matrix[row][col]
                if cell == minimumInRows[row] and cell == maximumInColumns[col]:
                    ans.append(cell)

        return ans

        
