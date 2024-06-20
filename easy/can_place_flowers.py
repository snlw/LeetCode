"""
https://leetcode.com/problems/can-place-flowers/submissions/1294687105

Time Complexity: O(n)
Space Complexity: O(1)

Type: Arrays
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        if len(flowerbed) == n:
            if n == 1 and flowerbed[0] == 0:
                return True
            return False

        count = 0

        if flowerbed[0] + flowerbed[1] == 0:
            flowerbed[0] = 1
            count += 1

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] + flowerbed[i - 1] + flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                count += 1

            if count >= n:
                return True
        
        if flowerbed[-1] + flowerbed[-2] == 0:
            flowerbed[-1] = 1
            count += 1

        return count == n
        
