"""
https://leetcode.com/problems/reverse-vowels-of-a-string/submissions/1294695686

Time Complexity: O(n)
Space Complexity: O(n)

Type: Strings
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        indexes = [i for i in range(len(s)) if s[i].lower() in vowels]
        
        splitted = [*s]

        for i in range(len(indexes) // 2):
            front = indexes[i]
            back = indexes[- 1 - i]
            splitted[front], splitted[back] = splitted[back], splitted[front]

        return "".join(splitted)
        
