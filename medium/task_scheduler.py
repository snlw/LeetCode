"""
https://leetcode.com/problems/task-scheduler/submissions/1316550297/

TC: O(n)
SC: O(1)

Type: Max Heap, Priority Queue
"""
class Solution:
     def leastInterval(self, tasks: List[str], n: int) -> int:
        # Build frequency map 
        frequency = [0] * 26
        for char in tasks:
            frequency[ord(char) - ord('A')] += 1

        # Max heap
        pq = [-f for f in frequency if f > 0]
        heapq.heapify(pq)

        time = 0
        # Process tasks until the heap is empty
        while pq:
            cycle = n + 1
            store = []
            count = 0
            while cycle > 0 and pq:
                current = -heapq.heappop(pq)
                if current > 1:
                    store.append(-(current - 1))
                count += 1
                cycle -= 1

            # Restore updated frequencies to the heap
            for x in store:
                heapq.heappush(pq, x)
            
            # Add time for the completed cycle
            time += count if not pq else n + 1
        return time
