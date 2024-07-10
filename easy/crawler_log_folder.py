"""
https://leetcode.com/problems/crawler-log-folder/submissions/1315815780/?envType=daily-question&envId=2024-07-10

TC: O(n)
SC: O(n)

Type: Stack
"""
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log == "../":
                if len(stack) == 0:
                    continue
                stack.pop()
            elif log == "./":
                continue
            else:
                stack.append(log)
        return len(stack)
        
