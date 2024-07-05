"""
https://leetcode.com/problems/3sum-closest/submissions/1310196261/

Time Complexity: O(n2)
Space Complexity: O(1)

Type: Two Pointers
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)

        ans = float("inf")
        diff = float("inf")

        nums.sort()

        for left in range(n - 2):
            mid = left + 1
            right = n - 1
            while mid < right:
                total = nums[left] + nums[mid] + nums[right]
                if total == target:
                    return total

                if total > target:
                    right -= 1
                elif total < target:
                    mid += 1
                
                localDiff = abs(total - target)
                if localDiff < diff:
                    ans = total
                    diff = localDiff

        return ans 
        
        
