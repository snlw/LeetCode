# https://leetcode.com/problems/reverse-string/submissions/1279725524/?envType=daily-question&envId=2024-06-06

# Time Complexity: O(n/2)
# Space Complexity: O(1)

# Type: String
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)

        for i in range(n // 2):
            temp = s[i]
            s[i] = s[n - i - 1]
            s[n - i - 1] = temp
