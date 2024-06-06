# https://leetcode.com/problems/hand-of-straights/submissions/1279719932/?envType=daily-question&envId=2024-06-06

# Time Complexity: O(n log n) ?
# Space Complexity: O(n)

# Type: Hashmap
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False

        frequency = dict()
        hand.sort()
        for card in hand:
            if card in frequency.keys():
                frequency[card] += 1
            else:
                frequency[card] = 1
        
        while sum(frequency.values()) != 0:
            available = [k for k, v in frequency.items() if v > 0]
            start = available[0]

            possible = True

            for i in range(1, groupSize):
                if start + i not in available:
                    possible = False
            
            if possible:
                for i in range(groupSize):
                    frequency[start + i] -= 1
            else:
                return False
            
        return True

        
