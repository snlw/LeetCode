# https://leetcode.com/problems/binary-search/submissions/1276337599/

# Time Complexity: O(log n)
# Space Complexity: O(1)

# Type: Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        # Edge Case where target is out of bounds
        if nums[left] > target or nums[right] < target:
            return -1

        while (left < right):
            mid = (right + left)//2
            value = nums[mid]

            if value == target:
                return mid
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1
                # Edge Case where nums is an array of 1

        if nums[left] == target:
            return left

        return -1 
            
