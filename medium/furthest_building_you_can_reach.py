"""
https://leetcode.com/problems/furthest-building-you-can-reach/submissions/1340467831/

TC: O(n * log n)
SC: O(n + k)

Type: Max Heap
"""
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        heapq.heapify(heap)
        n = len(heights)

        for i in range(n - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue
            
            bricks -= diff
            heapq.heappush(heap, -1 * diff)

            if bricks < 0:
                if ladders > 0:
                    ladders -= 1
                    saved = heapq.heappop(heap)
                    bricks += -1 * saved
                else:
                    return i
        
        return n - 1
