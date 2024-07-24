"""
https://leetcode.com/problems/simplify-path/submissions/1331887421/

TC: O(n)
SC: O(n)

Type: Stack
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = path.split("/")
        stack = []
        for directory in directories:
            if directory == "":
                continue

            if directory == "..":
                if stack:
                    stack.pop()
                continue
            
            if directory == ".":
                continue

            stack.append(directory)
        
        ans = "/" + "/".join(stack)
        return ans

        
