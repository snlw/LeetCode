"""
https://leetcode.com/problems/find-center-of-star-graph/submissions/1301647510/?envType=daily-question&envId=2024-06-27

Time Complexity: O(1)
Space Complexity: O(1)

Type: Star Graph
"""
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)

        for i in range(2):
            if edges[0][i] == edges[1][0] or edges[0][i] == edges[1][1]:
                return edges[0][i]

        
