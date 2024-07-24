"""
https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/1331520230/

TC: O(n log k)
SC: O(n)

Type: Max Heap, Min Heap
** O(n) answer requires Quick Select, see Lomuto Partition
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Input: [3,2,1,5,6,4]

        Heap State
        Initialized: [3, 2]
        Processing 1: [2, 3]
        Processing 5: [3, 5]
        Processing 6: [5, 6]
        Processing 4: [5, 6]
        """
        # Min Heap
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        return heap[0]

        # # Max heap
        # pq = [-num for num in nums]
        # heapq.heapify(pq)

        # ans = None
        # while k:
        #     ans = -heapq.heappop(pq)
        #     k -= 1

        # return ans
        
