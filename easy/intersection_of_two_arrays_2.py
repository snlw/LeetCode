"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/submissions/1307153801/?envType=daily-question&envId=2024-07-02

Time Complexity: O(n)
Space Complexity: O(n)

Type: Hash map
"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)

        if n1 >= n2:
            smaller = nums2
            longer = nums1
        else:
            smaller = nums1
            longer = nums2

        f = dict()
        for num in smaller:
            if num in f:
                f[num] += 1
            else:
                f[num] = 1

        ans = []
        for num in longer:
            if num in f and f[num] > 0:
                f[num] -= 1
                ans.append(num)
        
        return ans
