"""
https://leetcode.com/problems/reveal-cards-in-increasing-order/submissions/1356280064/

TC: O(n log n)
SC: O(n)

Type: Queue
"""
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        q = collections.deque()

        for i in range(n):
            q.append(i)
        
        deck.sort()

        ans = [-1] * n 
        for card in deck:
            ans[q.popleft()] = card

            if q:
                q.append(q.popleft())
        return ans

        # Iterative Method
        # n = len(deck)
        # deck.sort(reverse = True)
        
        # ans = [deck[0]]
        # for i in range(1, n):
        #     last = ans.pop()
        #     ans = [last] + ans
        #     ans = [deck[i]] + ans
