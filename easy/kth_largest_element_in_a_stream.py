"""
https://leetcode.com/problems/kth-largest-element-in-a-stream/submissions/1352829346/?envType=daily-question&envId=2024-08-12

TC: O(Nlogk)
SC: O(k)
"""
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = sorted(nums)[-k:] or []
        self.k = k
        heapq.heapify(self.heap)
        return

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)

        return self.heap[0]
