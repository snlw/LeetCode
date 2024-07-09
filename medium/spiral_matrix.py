"""
https://leetcode.com/problems/spiral-matrix/submissions/1315332363/

TC: O(m * n)
SC: O(m * n)
"""
class Solution:
     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        directionIdx = 0

        visited = set()
        cell = (0,0)
        ans = []

        while True:
            ## Update cell value into ans
            x, y = cell
            ans.append(matrix[x][y])
            visited.add(cell)

            ## Compute next cell
            dx, dy = direction[directionIdx]
            if not 0 <= x + dx < m or not 0 <= y + dy < n:
                directionIdx += 1
                if directionIdx == 4:
                    directionIdx = 0
                dx, dy = direction[directionIdx]

                if x + dx > m - 1 or y + dy > n - 1 or x + dx < 0 or y + dy < 0:
                    return ans

            cell = (x + dx, y + dy)
            ## If new cell is visited, we change direction
            if cell in visited:
                directionIdx += 1
                if directionIdx == 4:
                    directionIdx = 0
                dx, dy = direction[directionIdx]
                cell = (x + dx, y + dy)
                if cell in visited:
                    return ans
