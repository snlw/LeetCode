"""
https://leetcode.com/problems/incremental-memory-leak/submissions/1366775509/

TC: O(sqrt(m1 + m2))
SC: O(1)
"""
class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        req = 1

        while req:
            if memory1 >= memory2:
                if memory1 >= req:
                    memory1 -= req
                else:
                    break
            else:
                if memory2 >= req:
                    memory2 -= req
                else:
                    break
            req += 1

        return [req, memory1, memory2]


