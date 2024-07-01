"""
https://leetcode.com/problems/asteroid-collision/submissions/1306015311/

Time Complexity: O(n)
Space Complexity: O(n)

Type: Stack
"""
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]

        for asteroid in asteroids[1:]:
            if len(stack) == 0:
                stack.append(asteroid)
                continue
            ## Same Direction 
            if (asteroid > 0 and stack[-1] > 0) or (asteroid < 0 and stack[-1] < 0):
                stack.append(asteroid)
            else:
                crash = False
                if asteroid < 0:
                    while not crash and stack and asteroid < 0:
                        if asteroid + stack[-1] == 0:
                            stack.pop()
                            crash = True
                        elif asteroid + stack[-1] > 0:
                            crash = True
                        else:
                            stack.pop()
                            if len(stack) == 0 or stack[-1] < 0:
                                stack.append(asteroid)
                                break
                else:
                    stack.append(asteroid)

        return stack
                        



                

        
