# https://leetcode.com/problems/find-all-good-indices/submissions/1279562523/

# Time Complexity: O(n)
# Space Complexity: O(n)

# Type: DP
class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        left = [1] * n
        right = [1] * n

        left[0] = 0
        right[-1] = 0

        for i in range(2, n):
            if nums[i - 2] >= nums[i - 1]:
                left[i] = left[i - 1] + 1

        for i in range(n - 3, -1, -1):
            if nums[i + 2] >= nums[i + 1]:
                right[i] = right[i + 1] + 1

        ans = []

        for i in range(n):
            if left[i] >= k and right[i] >= k:
                ans.append(i)

        return ans

