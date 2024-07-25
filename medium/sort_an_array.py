"""
https://leetcode.com/problems/sort-an-array/submissions/1332577596/?envType=daily-question&envId=2024-07-25

TC: O(n log n)
SC: O(n)

Type: Heap Sort
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        result = []
        while nums:
            result.append(heapq.heappop(nums))
        return result
        
