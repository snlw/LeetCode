"""
https://leetcode.com/problems/kth-distinct-string-in-an-array/submissions/1344871092/?envType=daily-question&envId=2024-08-05
TC: O(n)
SC: O(n)

Type: Hash Map
"""
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        f = {}
        for s in arr:
            if s in f:
                f[s] += 1
            else:
                f[s] = 1
        distinct = [k for k,v in f.items() if v == 1]
        if len(distinct) >= k:
            return distinct[k - 1]
        return ""

