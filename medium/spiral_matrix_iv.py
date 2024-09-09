"""
https://leetcode.com/problems/spiral-matrix-iv/submissions/1384225526/?envType=daily-question&envId=2024-09-09

TC: O(n)
SC: O(m * n)
"""
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans = [[-1] * n for _ in range(m)]
        x = y = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        directionIdx = 0

        while head is not None:
            ans[x][y] = head.val
            dx, dy = directions[directionIdx]
            newx = x + dx
            newy = y + dy

            if not 0 <= newx < m or not 0 <= newy < n or ans[newx][newy] != -1:
                # Change direction
                directionIdx = (directionIdx + 1) % 4
            
            newdx, newdy = directions[directionIdx]
            x += newdx
            y += newdy
            head = head.next
        
        return ans
        
