"""
https://leetcode.com/problems/maximum-total-importance-of-roads/submissions/1303101610/?envType=daily-question&envId=2024-06-28

Time Complexity: O(n*2)
Space Complexity: O(n)

Type: Sort, Graph
"""
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        edges = [0 for _ in range(n)]

        for road in roads:
            edges[road[0]] += 1
            edges[road[1]] += 1

        edges.sort()

        importance = 1
        ans = 0
        for edge in edges:
            ans += edge * importance
            importance += 1

        return ans

        
