"""
https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/submissions/1305752923/

Time Complexity: O(n)
Space Complexity: O(1)

Type: Array
"""
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0

        for num in nums:
            if num % 3 == 1 or num % 3 == 2:
                count += 1
        
        return count

        
