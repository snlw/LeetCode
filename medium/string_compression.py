# https://leetcode.com/problems/string-compression/submissions/1279699568/

# Time Complexity: O(n)
# Space Complexity: O(1)

# Type: Two Pointers
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        answerIdx = 0
        i = 0 

        while i < n:
            char = chars[i]
            count = 0
            while i < n and chars[i] == char:
                count += 1
                i += 1
            
            chars[answerIdx] = char
            answerIdx += 1

            if count > 1:
                for c in str(count):
                    chars[answerIdx] = c
                    answerIdx += 1

        return answerIdx


        
