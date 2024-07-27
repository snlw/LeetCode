"""
https://leetcode.com/problems/minimum-cost-to-convert-string-i/submissions/1334660619/?envType=daily-question&envId=2024-07-27

TC: O(n ^ 3)
SC: O(n ^ 2)

Type: Graphs, Floyd-Warshall
"""
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        MAX = float('inf')

        def floydWarshall(start, end, cost):
            n = 26
            dist = [[MAX for _ in range(n)] for _ in range(n)]

            for i in range(n):
                dist[i][i] = 0
            
            for i in range(len(start)):
                startIndex = ord(start[i]) - ord('a')
                endIndex = ord(end[i]) - ord('a')
                dist[startIndex][endIndex] = min(dist[startIndex][endIndex], cost[i])
            
            for mid in range(n):
                for src in range(n):
                    for dest in range(n):
                        dist[src][dest] = min(dist[src][dest], dist[src][mid] + dist[mid][dest])
            return dist

        d = floydWarshall(original, changed, cost)

        ans = 0
        n = len(source)
        for i in range(n):
            sourceChar = ord(source[i]) - ord('a')
            targetChar = ord(target[i]) - ord('a')
            if sourceChar != targetChar:
                if d[sourceChar][targetChar] == MAX:
                    return -1
                ans += d[sourceChar][targetChar] 

        return ans if ans != MAX else -1
        
