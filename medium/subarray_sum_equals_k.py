"""
https://leetcode.com/problems/subarray-sum-equals-k/submissions/1314135239/

TC: O(n)
SC: O(n)

Type: Hash Table
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        table = dict([(0, 1)])
        ans = 0
        total = 0

        for num in nums:
            ## See Two Sum approach
            total += num
            if (total - k) in table:
                ans += table[total - k]
            
            if total in table:
                table[total] += 1
            else:
                table[total] = 1
        
        return ans
        
