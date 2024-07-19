"""
https://leetcode.com/problems/set-matrix-zeroes/solutions/5455461/beats-97-easy-to-understand-solution/

TC: O(m * n)
SC: O(m * n)
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        rowWithZeros = set()
        colWithZeros = set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rowWithZeros.add(i)
                    colWithZeros.add(j)

        for i in range(rows):
            if i in rowWithZeros:
                matrix[i] = [0] * cols
            else:
                for j in range(cols):
                    if j in colWithZeros:
                        matrix[i][j] = 0

