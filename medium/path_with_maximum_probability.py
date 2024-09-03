"""
https://leetcode.com/problems/path-with-maximum-probability/submissions/1377780648/?envType=daily-question&envId=2024-08-31
TC: O(n * E) where E is the number of edges
SC: O(n)
"""
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        maxProb = [0] * n
        maxProb[start_node] = 1 

        for _ in range(n - 1):
            updated = False
            for i, (src, dest) in enumerate(edges):
                prob = succProb[i]
                if maxProb[src] * prob > maxProb[dest]:
                    maxProb[dest] = maxProb[src] * prob
                    updated = True
                if maxProb[dest] * prob > maxProb[src]:
                    maxProb[src] = maxProb[dest] * prob
                    updated = True
            if not updated:
                break
        return maxProb[end_node]
