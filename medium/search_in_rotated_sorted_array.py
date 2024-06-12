"""
https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/1286074334/

Time Complexity: O(log n)
Space Complexity: O(1)

Type: Binary Search
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            isRightAscending = True
            for i in range(mid, right):
                if nums[i + 1] < nums[i]:
                    isRightAscending = False
                    break
            
            if isRightAscending:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1

        
