# https://leetcode.com/problems/height-checker/submissions/1283584149/?envType=daily-question&envId=2024-06-10

# Time Complexity: O(nlogn)
# Space Compleity: O(n)

# Type: Arrays
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n = len(heights)

        copy = sorted(heights)

        count = 0

        for i in range(n):
            if heights[i] != copy[i]:
                count += 1

        return count
        
