"""
https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/submissions/1334279901/?envType=daily-question&envId=2024-07-26

TC: O(n^3)
SC: O(n^2)

Type: Graphs, Floyd-Warshall
"""
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        def floydWarshall(edges, n):
            dist = [[float("inf") for _ in range(n)] for _ in range(n)]

            for i in range(n):
                dist[i][i] = 0

            for src, dest, weight in edges:
                dist[src][dest] = weight
                dist[dest][src] = weight
            
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])

            return dist

        distanceMatrix = floydWarshall(edges, n)

        neighbours = 10 ** 20
        city = None

        for i in range(n):
            distances = distanceMatrix[i]
            neighbourCount = len([c for c in distances if c <= distanceThreshold and c != 0])
            if neighbourCount <= neighbours:
                city = i
                neighbours = neighbourCount

        return city
        
