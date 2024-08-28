"""
https://leetcode.com/problems/count-sub-islands/submissions/1371211243/?envType=daily-question&envId=2024-08-28

TC: O(m * n)
SC: O(m * n)

Type: DFS
"""
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        R, C = len(grid1), len(grid1[0])
        ans = 0

        def flood(r, c):
            if grid2[r][c] == 1:
                grid2[r][c] = 2
            else:
                return
            
            if grid1[r][c] == 0:
                nonlocal isSubIsland
                isSubIsland = False
            
            if 0 <= r + 1 <= R - 1:
                flood(r + 1, c)
            if 0 <= r - 1 <= R - 1:
                flood(r - 1, c)
            if 0 <= c + 1 <= C - 1:
                flood(r, c + 1)
            if 0 <= c - 1 <= C - 1:
                flood(r, c - 1)

        for r in range(R):
            for c in range(C):
                cell = grid2[r][c]
                if cell == 0 or cell == 2:
                    continue

                isSubIsland = True
                flood(r, c)

                if isSubIsland:
                    ans += 1

        return ans
