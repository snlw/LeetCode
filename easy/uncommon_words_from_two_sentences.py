"""
https://leetcode.com/problems/uncommon-words-from-two-sentences/submissions/1392747854/?envType=daily-question&envId=2024-09-17
"""
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ans = set()
        
        freq1 = {}
        for word in s1.split():
            if word not in freq1:
                freq1[word] = 0
            freq1[word] += 1
        
        freq2 = {}
        for word in s2.split():
            if word not in freq2:
                freq2[word] = 0
            freq2[word] += 1

        together = s1 + " " + s2

        unique_words = set(together.split())

        for word in unique_words:
            if word in freq1 and word in freq2:
                if freq1[word] + freq2[word] == 1:
                    ans.add(word)
            elif word in freq1:
                if freq1[word] == 1:
                    ans.add(word)
            else:
                if freq2[word] == 1:
                    ans.add(word)

        return list(ans)

