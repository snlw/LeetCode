# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/submissions/1342784631/
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(arr) == sorted(target)
        
