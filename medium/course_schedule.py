"""
https://leetcode.com/problems/course-schedule/submissions/1284997301/

Time Complexity: O(n)
Space Complexity: O(n)

Type: Topological Sort, Kahn's Algorithm
"""
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        edges = prerequisites

        # Graph represented as an adjacency list
        adj = [[] for _ in range(n)]

        # Constructing adjacency list
        for edge in edges:
            adj[edge[0]].append(edge[1])
        
        def topological_sort(adj, V):
            # Vector to store indegree of each vertex
            indegree = [0] * V
            for i in range(V):
                for vertex in adj[i]:
                    indegree[vertex] += 1
        
            # Queue to store vertices with indegree 0
            q = deque()
            for i in range(V):
                if indegree[i] == 0:
                    q.append(i)
            result = []
            while q:
                node = q.popleft()
                result.append(node)
                # Decrease indegree of adjacent vertices as the current node is in topological order
                for adjacent in adj[node]:
                    indegree[adjacent] -= 1
                    # If indegree becomes 0, push it to the queue
                    if indegree[adjacent] == 0:
                        q.append(adjacent)
            return result

        graph = topological_sort(adj, n)

        # Check for cycle
        return len(graph) == n
