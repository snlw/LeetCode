"""
https://leetcode.com/problems/second-minimum-time-to-reach-destination/submissions/1336381765/?envType=daily-question&envId=2024-07-28

TC: O(n + e) 
SC: O(n)

Type: BFS
"""
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        ## Create an adjacency list
        graph = [[] for _ in range(n + 1)]
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)

        q = collections.deque([(1, 0)])
        visitedN = False
        times = [[] for _ in range(n+1)]

        while q:
            currentNode, t = q.popleft()

            if currentNode == n:
                if visitedN:
                    return t
                else:
                    visitedN = True

            if (t // change) % 2 == 1:
                wait = change - t % change
                t += wait
            t += time
            
            for nextNode in graph[currentNode]:
                visitTimes = times[nextNode]
                if len(visitTimes) == 0 or (len(visitTimes) == 1 and visitTimes[0] != t):
                    q.append((nextNode, t))
                    visitTimes.append(t)
