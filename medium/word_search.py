"""
https://leetcode.com/problems/word-search/submissions/1314050776/

TC: O(m * n * 4**len(word))
SC: O(len(word))

Type: DFS, Backtracking, Recursion
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        path = set()

        def dfs(r, c, target):
            if target == len(word):
                return True
            ## Out of Bounds
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return False
            ## Cell had been visited
            if (r,c) in path:
                return False
            ## Non matching character
            if word[target] != board[r][c]:
                return False
            
            path.add((r,c))
            res = (dfs(r + 1, c, target + 1) or dfs(r - 1, c, target + 1) or dfs(r, c - 1, target + 1) or dfs(r, c + 1, target + 1))

            path.remove((r,c))
            return res

        for i in range(rows):
            for j in range(cols):
                found = dfs(i, j, 0)
                if found:
                    return True

        return False

