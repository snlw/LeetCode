"""
https://leetcode.com/problems/01-matrix/submissions/1285840462/

Time Complexity: O(m * n)
Space Complexity: O(1)

Type: DP, Forward and Backward Traversal
"""
class Solution:
    def updateMatrix(self, mat):
        m = len(mat)
        n = len(mat[0])

        maxSize = 1e5

        ## From TOP-LEFT to BOTTOM-RIGHT, check top and left of cell
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    top = mat[i - 1][j] if i > 0 else maxSize
                    left = mat[i][j - 1] if j > 0 else maxSize
                    if top == 0 or left == 0:
                        mat[i][j] = 1
                    else:
                        mat[i][j] = 1 + min(top, left)

        ## From BOTTOM-RIGHT to TOP-LEFT, check bottom and right of cell
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] != 0:
                    bottom = mat[i + 1][j] if i < m - 1 else maxSize
                    right = mat[i][j + 1] if j < n - 1 else maxSize
                    if bottom == 0 or right == 0:
                        mat[i][j] = 1
                    else:
                        newMin = min(bottom, right) + 1
                        mat[i][j] = min(mat[i][j], newMin)

        return mat
