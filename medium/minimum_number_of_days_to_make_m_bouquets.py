"""
https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/submissions/1293590428

Time Complexity: O(n log m) where m is max(bloomDay) - min(bloomDay)
Space Complexity: O(1)

Type: Binary Search, Brute Force 
"""
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        left = 0 
        right = 10 ** 9 

        ans = -1

        while left <= right:
            mid = (left + right) // 2
            consecutive = 0 
            bouquets = 0
            for bloom in bloomDay:
                if bloom <= mid:
                    consecutive += 1
                    if consecutive >= k:
                        bouquets += 1
                        consecutive = 0
                else:
                    consecutive = 0
            if bouquets >= m:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
