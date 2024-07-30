"""
https://leetcode.com/problems/bag-of-tokens/submissions/1338136342/?envType=daily-question&envId=2024-07-30

TC: O(n)
SC: O(1)

Type: Greedy
"""
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0

        while len(tokens) > 0:
            if score == 0:
                if power >= tokens[0]:
                    power -= tokens[0]
                    tokens.pop(0)
                    score += 1
                else:
                    return score
            elif power < tokens[0]:
                if len(tokens) == 1:
                    return score
                power += tokens[-1]
                tokens.pop()
                score -= 1
            else:
                power -= tokens[0]
                tokens.pop(0)
                score += 1
        return score
