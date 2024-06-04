# https://leetcode.com/problems/contains-duplicate/submissions/1277488796/

# Time Complexity: O(n)
# Space Complexity: O(n)

# Type: Hash Set

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        originalLength = len(nums)
        uniqueLength = len(set(nums))

        return originalLength != uniqueLength
        
