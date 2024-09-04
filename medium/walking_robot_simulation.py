"""
https://leetcode.com/problems/walking-robot-simulation/submissions/1378849924/?envType=daily-question&envId=2024-09-04
"""
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ans = 0
        currentPosition = (0,0)
        currentDirectionIndex = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for command in commands:
            if command == -1:
                currentDirectionIndex = (currentDirectionIndex + 1) % 4
                continue
            elif command == -2:
                currentDirectionIndex = (currentDirectionIndex - 1) % 4
                continue
            else:
                dx, dy = directions[currentDirectionIndex]
                x, y = currentPosition
                newx = x + command * dx
                newy = y + command * dy
                if dx == 0:
                    obs = [o[1] for o in obstacles if o[0] == x]
                    if len(obs) > 0:
                        for ob in sorted(obs):
                            if y < ob <= newy:
                                newy = ob - 1
                                break
                            elif newy <= ob < y:
                                newy = ob + 1
                                break
                if dy == 0:
                    obs = [o[0] for o in obstacles if o[1] == y]
                    if len(obs) > 0:
                        for ob in sorted(obs):
                            if x < ob <= newx:
                                newx = ob - 1
                                break    
                            elif newx <= ob < x:
                                newx = ob + 1
                                break         
                ans = max(ans, newx**2 + newy**2)
                currentPosition = (newx, newy)
        return ans
        
