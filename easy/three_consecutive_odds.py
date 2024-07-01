"""
https://leetcode.com/problems/three-consecutive-odds/submissions/1305579281/?envType=daily-question&envId=2024-07-01

Time Complexity: O(n)
Space Complexity: O(1)

Type: Arrays
"""
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        oddCount = 0
        n = len(arr)

        for i in range(n):
            if arr[i] % 2 == 1:
                oddCount += 1
            else:
                oddCount = 0
            
            if oddCount == 3:
                return True

        return False

        
