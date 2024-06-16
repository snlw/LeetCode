"""
https://leetcode.com/problems/patching-array/submissions/1290242242

Time Complexity: O(n)
Space Complexity: O(1)

Type: Greedy
"""
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        count = 0
        right = 0
        for num in nums:
            while n > right and num > right + 1:
                right += right + 1
                count += 1
            right += num
        
        while n > right:
            right += right + 1
            count += 1

        return count 
            
