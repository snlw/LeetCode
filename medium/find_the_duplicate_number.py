"""
https://leetcode.com/problems/find-the-duplicate-number/submissions/1317619228/

TC: O(n)
SC: O(1)

Type: Floyd's Cycle Algorithm
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = nums[0]
        hare = nums[0]

        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        a = nums[0]
        b = tortoise
        while a != b:
            a = nums[a]
            b = nums[b] 

        return a
