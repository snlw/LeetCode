# https://leetcode.com/problems/two-sum/?source=submission-ac

# Time Complexity: O(n)
# Space Complexity: O(n)

# Type: Hash Table

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} 
        for i in range(len(nums)):
            difference_to_make_up_target = target - nums[i]
            if difference_to_make_up_target in hashmap:
                return [i, hashmap[difference_to_make_up_target]]
            
            hashmap[nums[i]] = i


        
        
