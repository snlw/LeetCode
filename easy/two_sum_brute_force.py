# https://leetcode.com/problems/two-sum/submissions/1273022407/

# Example
# nums : [1, 3, 5, 7, 9]
# target: 10
# Find indexes of L + R = target 
# i.e L = 0 and R = 4

# while looping : 
#   current_index = 0;
#   first_number = 1;
#   difference_to_make_up_target = 10 - 1 = 9;
#   search from index 1 to end, check if difference_to_make_up_target exists.

# Time Complexity: O(n2)
# Space Complexity: O(1)

# Type: Brute Force

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = len(nums)
        for left_index in range(0, numbers):
            difference_to_make_up_target = target - nums[left_index]
            rest_of_numbers = nums[left_index+1:]
            if difference_to_make_up_target in rest_of_numbers:
                right_index = rest_of_numbers.index(difference_to_make_up_target)
                return [left_index, left_index + 1 + right_index]


        
        
