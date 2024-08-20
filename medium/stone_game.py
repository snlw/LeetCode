"""
https://leetcode.com/problems/stone-game/submissions/1362129221/

TC: O(n)
SC: O(1)

Type: Stack
"""
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        """
        TC, SC: O(1)
        
        Description: Alice clearly always wins the 2 pile game. With some effort, we can see that she always wins the 4 pile game.

If Alice takes the first pile initially, she can always take the third pile. If she takes the fourth pile initially, she can always take the second pile. At least one of first + third, second + fourth is larger, so she can always win.

We can extend this idea to N piles. Say the first, third, fifth, seventh, etc. piles are white, and the second, fourth, sixth, eighth, etc. piles are black. Alice can always take either all white piles or all black piles, and one of the colors must have a sum number of stones larger than the other color.

Hence, Alice always wins the game.

        return True
        """
        alice, bob = 0, 0
        piles.sort()

        i = 0
        while piles:
            if i % 2 == 0:
                alice += piles.pop()
            else:
                bob += piles.pop()
            i += 1
        
        return alice > bob
