"""
https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/submissions/1326959065/

TC: O(m * n)
SC: O(m * n)
"""
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        ans = [[0 for _ in range(n)] for _ in range(m)]

        MAX_SUM_ROWS = m * (10**9)
        MAX_SUM_COLS = n * (10**9)

        def getIndexOfMinimum(arr):
            minimumValue = min(arr)
            for i in range(len(arr)):
                if arr[i] == minimumValue:
                    return i

        while sum(rowSum) != MAX_SUM_ROWS and sum(colSum) != MAX_SUM_COLS:
            rowMinimum = getIndexOfMinimum(rowSum)
            colMinimum = getIndexOfMinimum(colSum)
            value = min(rowSum[rowMinimum], colSum[colMinimum])
            ans[rowMinimum][colMinimum] = value
            rowSum[rowMinimum] -= value
            colSum[colMinimum] -= value
            if rowSum[rowMinimum] == 0:
                rowSum[rowMinimum] = 10 ** 9 
            if colSum[colMinimum] == 0:
                colSum[colMinimum] = 10 ** 9 

        return ans


