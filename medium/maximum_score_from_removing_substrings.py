"""
https://leetcode.com/problems/maximum-score-from-removing-substrings/submissions/1318383782/?envType=daily-question&envId=2024-07-12

TC: O(n)
SC: O(n)

Type: Stack, Two Pass, Greedy
"""
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        n = len(s)
        stack = []

        if x > y:
            best = ['a', 'b']
            subBest = ['b', 'a']
        else:
            best = ['b', 'a']
            subBest = ['a', 'b']

        ans = 0

        for i in range(n):
            if stack:
                if s[i] == best[-1] and stack[-1] == best[0]:
                    ans += max(x, y)
                    stack.pop()
                    continue

            stack.append(s[i])

        subStack = []

        for i in range(len(stack)):
            if subStack:
                if stack[i] == subBest[-1] and subStack[-1] == subBest[0]:
                    ans += min(x, y)
                    subStack.pop()
                    continue

            subStack.append(stack[i])

        return ans
