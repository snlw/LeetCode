"""
https://leetcode.com/problems/maximum-score-from-removing-stones/submissions/1388776710/
"""
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        heap = [-a, -b, -c]
        heapq.heapify(heap)

        ans = 0

        while sum(heap) < 0:
            if heap[1] == 0 and heap[2] == 0:
                break
            largest = -heapq.heappop(heap)
            middle = -heapq.heappop(heap)

            ans += 1
            heapq.heappush(heap, -largest + 1)
            heapq.heappush(heap, -middle + 1)
        
        return ans
