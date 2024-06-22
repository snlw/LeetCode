"""
https://leetcode.com/problems/count-number-of-nice-subarrays/submissions/1296840258/

Time Complexity: O(n)
Space Comeplexity: O(1)

Type: Prefix Sum
"""
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        for i in range(n):
            nums[i] %= 2

        prefixCount = [0] * (n + 1)
        prefixCount[0] = 1
        s = 0 
        ans = 0

        for num in nums:
            s += num
            if s >= k:
                ans += prefixCount[s - k]
            prefixCount[s] += 1
        
        return ans

