"""
https://leetcode.com/problems/number-of-atoms/submissions/1320528914/

TC: O(n ^ 2)
SC: O(n)

Type: Stack
"""
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        n = len(formula)
        idx = 0

        while idx < n:
            if formula[idx] == ")":
                move = False
                ## Count and push it back in to the stack
                numberOfGroups = "1"
                if idx + 1 < n and formula[idx + 1].isdigit():
                    numberOfGroups = formula[idx + 1]

                    ## When the number of groups > 10
                    if idx + 2 < n and formula[idx + 2].isdigit():
                        numberOfGroups += formula[idx + 2]
                        idx += 1
                    move = True

                miniStack = []
                while stack[-1] != "(":
                    miniStack.append(stack.pop())
                ## Remove the open parentheses
                stack.pop()

                miniStack = miniStack[::-1]

                while miniStack:
                    char = miniStack.pop()
                    if char.isdigit():
                        ele = miniStack.pop()
                        stack.append(ele)
                        stack.append(str(int(char) * int(numberOfGroups)))
                    else:
                        stack.append(char)
                        if numberOfGroups != "1":
                            stack.append(numberOfGroups)
                if move:
                    idx += 1
            else:
                if formula[idx].islower():
                    stack[-1] += formula[idx]
                elif formula[idx].isdigit():
                    if stack[-1].isdigit():
                        ## Multiple digit
                        stack[-1] += formula[idx]
                    else:
                        ## Single digit
                        stack.append(formula[idx])
                else:
                    stack.append(formula[idx])
            idx += 1

        ## Convert to dict
        idx2 = 0
        frequency = dict()
        while idx2 < len(stack):
            ele = stack[idx2]
            if idx2 + 1 < len(stack) and stack[idx2 + 1].isdigit():
                if ele in frequency:
                    frequency[ele] += int(stack[idx2 + 1])
                else:
                    frequency[ele] = int(stack[idx2 + 1])
                idx2 += 1
            else:
                if ele in frequency:
                    frequency[ele] += 1
                else:
                    frequency[ele] = 1
            idx2 += 1

        ## Reorder
        ans = ""
        sortedFrequency = sorted(list(frequency.items()))
        for element, count in sortedFrequency:
            ans += element
            if count != 1:
                ans += str(count)
        return ans
