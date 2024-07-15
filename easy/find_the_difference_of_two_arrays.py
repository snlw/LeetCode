"""
https://leetcode.com/problems/find-the-difference-of-two-arrays/submissions/1321571159/?envType=study-plan-v2&envId=leetcode-75

TC: O(n + m)
SC: O(n + m)

Type: Hash map
"""
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        def getFrequency(arr):
            f = dict()
            for num in set(arr):
                if num not in f:
                    f[num] = True
            return f
        
        f1 = getFrequency(nums1)
        f2 = getFrequency(nums2)

        def check(f, arr):
            ans = []
            for num in set(arr):
                if num not in f:
                    ans.append(num)
            return ans
        
        return [check(f2, nums1), check(f1, nums2)]
        
        
