"""
https://leetcode.com/problems/daily-temperatures/submissions/1321551287/

TC: O(n)
SC: O(n)

Type: Monotonic Stack
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        stack, ans = [], []

        for i in range(n):
            current = temperatures[i]
            while stack:
                prev, prevIdx = stack[-1]
                if current > prev:
                    # (days, idx)
                    ans.append((i - prevIdx, prevIdx))
                    stack.pop()
                else:
                    break

            stack.append((current, i))
        
        for j in range(len(stack)):
            ans.append((0, stack[j][1]))
        
        sortedByIdx = sorted(ans, key=lambda x:x[1])

        return [x[0] for x in sortedByIdx]

