"""
https://leetcode.com/problems/equal-row-and-column-pairs/submissions/1321577433/?envType=study-plan-v2&envId=leetcode-75

TC: O(n ^ 2)
SC: O(n)

Type: Hash Map
"""
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)

        rowsHashMap = dict()
        for row in grid:
            rowStringified = str(row)
            if rowStringified in rowsHashMap:
                rowsHashMap[rowStringified] += 1
            else:
                rowsHashMap[rowStringified] = 1

        ans = 0
        for i in range(n):
            col = [row[i] for row in grid]
            colStringified = str(col)
            if colStringified in rowsHashMap:
                ans += rowsHashMap[colStringified]

        return ans
        
