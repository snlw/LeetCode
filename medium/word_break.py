"""
https://leetcode.com/problems/word-break/submissions/1310576841/

Time Complexity: O(n3+m⋅k)
Space Complexity: O(n + m.k)

Type: BFS
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        queue = collections.deque([0])
        seen = set()

        while queue:
            start = queue.popleft()
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if end not in seen:
                    sub = s[start:end]
                    if sub in words:
                        queue.append(end)
                        seen.add(end)
        return False


        
