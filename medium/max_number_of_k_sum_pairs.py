"""
https://leetcode.com/problems/max-number-of-k-sum-pairs/submissions/1299913264/?envType=study-plan-v2&envId=leetcode-75

Time Complexity: O(n)
Space Complexity: O(n)

Type: Hashmap
"""
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        f = dict()
        n = len(nums)

        for i in range(n):
            if nums[i] in f.keys():
                f[nums[i]] += 1
            else:
                f[nums[i]] = 1
        ans = 0
        for key,value in f.items():
            corresponding = k - key
            if corresponding not in f.keys():
                continue
            if corresponding == key:
                op = value // 2
                print(op)
                ans += op
                f[key] = value % 2
            else:
                op = min(value, f[corresponding])
                ans += op
                f[key] -= op
                f[corresponding] -= op

        return ans
