"""
https://leetcode.com/problems/maximum-swap/submissions/1335256189/

TC: O(n)
SC: O(n)

Type: Hash Map
"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        freq = dict()
        s = [*str(num)]
        for i in range(len(s)):
            char = s[i]
            if char in freq:
                freq[char].append(i)
            else:
                freq[char] = [i]

        idx = 0
        for i in range(9, -1, -1):
            digit = str(i)
            if digit in freq:
                positions = freq[digit]
                count = len(positions)
                while count:
                    if idx not in positions:
                        s[idx], s[positions[-1]] =  s[positions[-1]], s[idx]
                        return int("".join(s))
                    idx += 1
                    count -= 1

        return num

