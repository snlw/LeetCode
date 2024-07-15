"""
https://leetcode.com/problems/dota2-senate/submissions/1321894752/?envType=study-plan-v2&envId=leetcode-75

TC: O(n)
SC: O(n)

Type: Queue
"""
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = collections.deque([*senate])
        streak = []

        while queue:
            ## Check if the queue is all R or D
            if len(list(set(queue))) == 1:
                return "Radiant" if queue[0] == "R" else "Dire"

            banned = False
            curr = queue.popleft()
            if len(streak) == 0:
                streak.append(curr)
            else:
                if streak[0] == curr:
                    streak.append(curr)
                elif streak and streak[0] != curr:
                    streak.pop()
                    banned = True
            if not banned:
                queue.append(curr)
