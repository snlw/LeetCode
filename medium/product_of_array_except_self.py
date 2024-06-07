# https://leetcode.com/problems/product-of-array-except-self/submissions/1280121457/

# Time Complexity: O(n)
# Space Complexity: O(n)

# Type: Prefix Product, Suffix Product
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [nums[0]]
        suffix = [nums[-1]] 

        for i in range(1, n):
            prefix.append(prefix[i - 1] * nums[i])
            suffix.append(suffix[i - 1] * nums[-i - 1])

        suffix.reverse()

        ans = []

        for i in range(n):
            if i == 0:
                ans.append(suffix[i + 1])
            elif i == n - 1:
                ans.append(prefix[i - 1])
            else:
                ans.append(prefix[i - 1] * suffix[i + 1])

        return ans


