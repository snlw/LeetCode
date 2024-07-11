"""
https://leetcode.com/problems/text-justification/submissions/1317351011/

TC: O(n)
SC: O(n * m)

Type: Greedy
"""
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        left = 0
        leftJustify = []
        lines = []
        line = []

        while left < n:
            word = words[left]
            line.append(word)

            if len(" ".join(line)) > maxWidth:
                extra = line.pop()
                if len(line) == 1:
                    leftJustify.append(len(lines))
                lines.append(line)
                line = [extra]
                if left == n - 1:
                    leftJustify.append(len(lines))
                    lines.append([extra])
            elif left == n - 1:
                leftJustify.append(len(lines))
                lines.append(line)

            left += 1
        ans = []

        for i in range(len(lines)):
            if i in leftJustify:
                current = lines[i]
                currentWithSpace = " ".join(current)
                whitespaces = maxWidth - len(currentWithSpace)
                ans.append(currentWithSpace + " "*whitespaces)
            else:
                current = lines[i]
                whitespaces = maxWidth - len("".join(current))
                slots = len(current) - 1
                whitespacePerSlot = whitespaces // slots
                extra = whitespaces % slots
                newline = current[0]
                for j in range(1, len(current)):
                    if j == len(current) - 1:
                        newline += whitespacePerSlot * " "
                    else:
                        newline += whitespacePerSlot * " "
                        if extra:
                            newline += " "
                            extra -= 1
                    newline += current[j]
                ans.append(newline)

        return ans
