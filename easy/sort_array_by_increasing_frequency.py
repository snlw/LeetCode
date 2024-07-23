"""
https://leetcode.com/problems/sort-array-by-increasing-frequency/submissions/1330135682/?envType=daily-question&envId=2024-07-23

TC: O(n)
SC: O(n)
"""
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = collections.Counter(nums)
        s = sorted(sorted(freq.items(), key=lambda x:x[0], reverse=True), key=lambda x:x[1])
        ans = []
        for val, f in s:
            ans += [val] * f
        return ans
        
