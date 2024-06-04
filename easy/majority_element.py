# https://leetcode.com/problems/majority-element/submissions/1277496896/
# Time Complexity: O(n)
# Space Complexity: O(n)

# Type: Unordered Map

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        frequency = dict()

        for number in nums:
            if str(number) in frequency:
                frequency[str(number)] += 1
                if frequency[str(number)] > len(nums)//2:
                    return number
            else:
                frequency[str(number)] = 1
        
