"""
https://leetcode.com/problems/minimum-height-trees/submissions/1317045002/

TC: O(n)
SC: O(n)

Type: Graph, BFS
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        ## Create adjacency list
        graph = defaultdict(list)
        for source, destination in edges:
            graph[source].append(destination)
            graph[destination].append(source)

        edgeCount = {}
        leaves = collections.deque()
        for node, neighbors in graph.items():
            if len(neighbors) == 1:
                leaves.append(node)
            edgeCount[node] = len(neighbors)

        while leaves:
            if n <= 2:
                return list(leaves)

            for i in range(len(leaves)):
                leaf = leaves.popleft()
                n -= 1
                for neighbor in graph[leaf]:
                    edgeCount[neighbor] -= 1
                    if edgeCount[neighbor] == 1:
                        leaves.append(neighbor)

        ## For n == 1 and edges == []
        return [0]
