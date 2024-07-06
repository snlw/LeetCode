"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/submissions/1311287470/

TC: O(n2)
SC: O(n)

Type: Sliding Window
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        window = len(p)
        chars = sorted([*p])

        ans = []
        for i in range(n - window + 1):
            sub = [*s[i:i + window]]
            if sorted(sub) == chars:
                ans.append(i)
        return ans
