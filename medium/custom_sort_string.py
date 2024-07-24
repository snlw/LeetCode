"""
https://leetcode.com/problems/custom-sort-string/submissions/1331532970/

Type: Hash Map
"""
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        TC: O(n)
        SC: O(n)
        """
        freq = dict()
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        ans = ""
        for orderedChar in order:
            if orderedChar in freq:
                ans += orderedChar * freq[orderedChar]
                freq[orderedChar] = 0
        
        ## Check for characters that do not appear in order
        notInOrderChars = [k * v for k, v in freq.items() if v > 0]
        for substring in notInOrderChars:
            ans += substring

        return ans

        """
        This approach is to sort by index position when given order.
        This requires extra space and extra time O(n) to sort
        orderMapper = dict()
        for i, v in enumerate(order):
            orderMapper[v] = i

        charIndexTuples = []
        for char in s:
            charIndexTuples.append((char, orderMapper[char] if char in orderMapper else -1))

        charIndexTuples = sorted(charIndexTuples, key=lambda x: x[1])

        return "".join([x[0] for x in charIndexTuples])
        """
        
