"""
https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/submissions/1286597952/

Time Complexity: O(n)
Space Complexity: O(1)

Type: Greedy
"""
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        n = len(seats)

        seats.sort()
        students.sort()

        moves = 0 

        for i in range(n):
            moves += abs(seats[i] - students[i])

        return moves
        
