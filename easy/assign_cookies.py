"""
https://leetcode.com/problems/assign-cookies/submissions/1386561978/
"""
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        ans = 0
        for cookie in s:
            for i, child in enumerate(g):
                if child == -1:
                    continue
                if cookie >= child:
                    ans += 1
                    g[i] = -1 
                break
        return ans

            
