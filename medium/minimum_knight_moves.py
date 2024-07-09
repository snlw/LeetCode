"""
TC: O((max(abs(x), abs(y)))^2)
SC: O((max(abs(x), abs(y)))^2)

Type: BFS
"""
class Solution:
    def minKnightMoves(self, x:int, y:int) -> int:
        queue = collections.deque([(0, 0)])
        visited = set([(0, 0)])
        destinationCoordinates = [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)]
        ans = 0

        while queue:
            for _ in range(len(queue)):
                currentX, currentY = queue.popleft()

                if currentX == x and currentY == y:
                    return ans

                for dx, dy in destinationCoordinates:
                    destination = (currentX + dx, currentY + dy)
                    if destination not in visited:
                        queue.append(destination)
                        visited.add(destination)
            ans += 1

        return -1
