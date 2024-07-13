"""
https://leetcode.com/problems/robot-collisions/submissions/1319780148/

TC: O(n log n)
SC: O(n)

Type: Monotonic Stack
"""
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robots = sorted([[positions[i], healths[i], directions[i], i] for i in range(n)], key=lambda x:x[0])
        stack = []

        for i in range(n):
            if len(stack) == 0:
                stack.append(robots[i])
                continue
            
            currentPosition, currentHealth, currentDirection, currentIdx = robots[i]
            alive = True

            ## Robot collides
            if currentDirection == 'R':
                stack.append(robots[i])
            else:
                while stack:
                    prevPosition, prevHealth, prevDirection, prevIdx = stack[-1]
                    if prevDirection == 'R':
                        if prevHealth == currentHealth:
                            alive = False
                            stack.pop()
                            break
                        elif currentHealth > prevHealth:
                            stack.pop()
                            currentHealth -= 1
                        else:
                            stack[-1] = [prevPosition, prevHealth - 1, prevDirection, prevIdx]
                            alive = False
                            break
                    else:
                        break

                if alive:
                    stack.append((currentPosition, currentHealth, currentDirection, currentIdx))
        
        ## Sort by initial order at the end
        posDecreasing = sorted(stack, key=lambda x:x[3])
        return [x[1] for x in posDecreasing]

            


            

