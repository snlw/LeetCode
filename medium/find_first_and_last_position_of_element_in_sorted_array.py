"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/1310211331/

Time Complexity: O(log n)
Space Complexity: O(1)

Type: Binary Search
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        if n == 0:
            return [-1, -1]
        
        if n == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        left = 0
        right = n - 1

        matchingIdx = -1

        while left < right:
            if nums[left] == target:
                matchingIdx = left
                break
            
            if nums[right] == target:
                matchingIdx = right
                break

            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                matchingIdx = mid
                break

        if matchingIdx == -1:
            return [-1, -1]
        
        start = matchingIdx
        end = matchingIdx

        for i in range(matchingIdx - 1, -1, -1):
            if nums[i] == target:
                start = i
            else:
                break
        
        for i in range(matchingIdx + 1, n):
            if nums[i] == target:
                end = i
            else:
                break

        return [start, end]
        
