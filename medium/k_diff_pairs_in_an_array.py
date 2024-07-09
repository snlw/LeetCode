"""
https://leetcode.com/problems/k-diff-pairs-in-an-array/submissions/1314924040/

TC: O(n)
SC: O(n)

Type: Hash Map
"""
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        unique = set(nums)
        f = dict()
        for num in nums:
            if num in f:
                f[num] += 1
            else:
                f[num] = 1

        ans = set()

        if k == 0:
            for k, v in f.items():
                if v >= 2:
                    ans.add((k, k))
        else:
            for num in unique:
                possible = [num + k, num - k]
                for p in possible:
                    if p in f:
                        ans.add((min(num, p), max(num, p)))
        
        return len(ans)
            
            
        
