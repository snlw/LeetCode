# https://leetcode.com/problems/maximum-subarray/submissions/1277566482/

# Time Complexity: O(n)
# Space Complexity: O(1)

# Type: Kadane's Algorithm 
# local_max(i) = max(A[i], local_max(i - 1) + A[i])
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = -10**4 - 1
        local_maximum = 0
        for x in nums:
            local_maximum = max(x, local_maximum + x)
            answer = max(answer, local_maximum)
        return answer
        
