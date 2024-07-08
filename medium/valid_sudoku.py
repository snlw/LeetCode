"""
https://leetcode.com/problems/valid-sudoku/submissions/1313698781/

TC: O(1)
SC: O(1)
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isUnique(nums: List[str]):
            numbers = [c for c in nums if c.isdigit()]
            unique = set(numbers)
            if len(numbers) != len(unique):
                return False
            return True

        def columnValid(i):
            col = [row[i] for row in board]
            return isUnique(col)
        
        def rowValid(i):
            row = board[i]
            return isUnique(row)
        
        def squareValid(i, j):
            square = []
            rows = board[j:j+3]
            for row in rows:
                square += row[i:i+3]
            return isUnique(square)

        ## Check rows and columns
        for i in range(9):
            if not rowValid(i) or not columnValid(i):
                return False
        
        ## Check squares
        coordinates = [(0,0), (3,0), (6,0), (0,3), (3,3), (6,3), (0,6), (3,6), (6,6)]
        for (i, j) in coordinates:
            if not squareValid(i, j):
                return False

        return True
        
