"""
https://leetcode.com/problems/filling-bookcase-shelves/submissions/1339324774/?envType=daily-question&envId=2024-07-31

TC: O(n ^ 2)
SC: O(n)

Type: Partition DP
"""
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)

        dp = [0]

        for i in range(n):
            totalHeight = float('inf')
            width = 0
            maxHeight = 0
            for j in range(i, -1, -1):
                thickness, height = books[j]
                width += thickness
                maxHeight = max(maxHeight, height)
                if width > shelfWidth:
                    break
                totalHeight = min(totalHeight, dp[j] + maxHeight)
            dp.append(totalHeight)

        return dp[-1]

        
