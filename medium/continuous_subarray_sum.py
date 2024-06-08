# https://leetcode.com/problems/continuous-subarray-sum/submissions/1281882902/?envType=daily-question&envId=2024-06-08

# Time Complexity: O(n)
# Space Complexity: O(k)

# Type: Hash Map, Prefix Sum
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        map = {0: -1}
        sum = 0

        for i in range(n):
            sum += nums[i]
            rem = sum % k 

            if rem in map:
                if i - map[rem] > 1:
                    return True
            else:
                map[rem] = i

        return False
