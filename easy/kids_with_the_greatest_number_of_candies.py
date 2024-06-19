"""
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/submissions/1293542465

Time Complexity: O(n)
Space Complexity: O(1)

Type: Greedy
"""
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        ans = []

        for i in range(n):
            temp = candies[:]
            temp[i] += extraCandies
            maximum = max(temp)
            if temp[i] >= maximum:
                ans.append(True)
            else:
                ans.append(False)

        return ans
        
