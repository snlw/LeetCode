"""
https://leetcode.com/problems/network-delay-time/submissions/1316503439/

TC: O(E log V), where E is the number of edges and V is the number of vertices
SC: O(V + E)

Type: BFS
"""
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ## Construct an adjacency list
        graph = collections.defaultdict(list)
        for u, v, c in times:
            graph[u - 1].append((v - 1, c))
        
        queue = collections.deque([(k - 1, 0)])

        MAX_TIME = 6001
        minTime = [MAX_TIME for _ in range(n)]
        minTime[k - 1] = 0

        while(queue):
            current, carry = queue.popleft()
            for neighbor, cost in graph[current]:
                if carry + cost < minTime[neighbor]:
                    minTime[neighbor] = carry + cost
                    queue.append((neighbor, carry + cost))

        if MAX_TIME in minTime:
            return -1

        return max(minTime)
