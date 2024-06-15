"""
https://leetcode.com/problems/ipo/submissions/1289149726

Time Complexity: O(nlogn + klogn)
Space Complexity: O(n)

Type: Max Heap, Greedy
"""
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        projects = sorted(zip(capital, profits), key=lambda x:x[0], reverse=True)

        for _ in range(k):
            while projects and projects[-1][0] <= w:
                p = projects.pop()[1]
                heappush(heap, -p)
            if heap:
                w -= heappop(heap)
        
        return w
