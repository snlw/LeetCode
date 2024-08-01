"""
https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/submissions/1340800496/

TC: O(n)
SC: O(n)

Type: Hash Map
"""
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        f = {}
        for num in arr:
            if num in f:
                f[num] += 1
            else:
                f[num] = 1
        
        occurrences = sorted(f.items(), key=lambda x:x[1])
        idx = 0
        while k > 0:
            if k >= occurrences[idx][1]:
                k -= occurrences[idx][1]
                idx += 1
            else:
                break

        return len(occurrences[idx:])
