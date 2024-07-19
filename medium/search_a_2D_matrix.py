"""
https://leetcode.com/problems/search-a-2d-matrix/submissions/1326100184/

TC: O(log m + log n)
SC: O(1)

Type: Binary Search
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bot = rows - 1
        while top <= bot:
            mid = (top + bot) // 2
            value = matrix[mid]
            if matrix[mid][0] < target < matrix[mid][-1]:
                break
            elif matrix[mid][0] > target:
                bot = mid - 1
            else:
                top = mid + 1
        
        targetRow = matrix[(top + bot) // 2]
        
        left = 0
        right = cols - 1
        while left < right:
            mid = (left + right) // 2
            value = targetRow[mid]
            if value == target:
                return True
            if value > target:
                right = mid - 1
            else:
                left = mid + 1

        return targetRow[left] == target
        
