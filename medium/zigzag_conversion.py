"""
https://leetcode.com/problems/zigzag-conversion/submissions/1307234655/

Time Complexity: O(n)
Space Complexity: O(n)

Type: String
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        ans = [[] for _ in range(numRows)]

        counter = 0

        additive = True

        while s:
            char = s[0]
            ans[counter].append(char)

            if additive:
                counter += 1
            else:
                counter -= 1
            
            if counter == numRows:
                counter -= 2
                additive = False

            if counter == -1:
                counter += 2
                additive = True

            s = s[1:]

        return "".join(["".join(row) for row in ans])
