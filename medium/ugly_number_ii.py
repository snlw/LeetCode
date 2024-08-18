"""
https://leetcode.com/problems/ugly-number-ii/submissions/1360369671/?envType=daily-question&envId=2024-08-18

TC: O(n log n)
SC: O(m) where is the number of unique ugly numbers

Type: Min Heap
"""
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1

        heap = [1]
        heapq.heapify(heap)

        factors = [2, 3, 5]

        while n - 1:
            prev = heapq.heappop(heap)
            for f in factors:
                new = f * prev
                if new not in heap:
                    heapq.heappush(heap, new)
            n -= 1
        
        return heapq.heappop(heap)


