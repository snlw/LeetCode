# https://leetcode.com/problems/sum-game/submissions/1279269329/

# Time Complexity: O(n)
# Space Complexity: O(n)

# Type: Game Theory
class Solution:
    def sumGame(self, num: str) -> bool:
        alice = True
        bob = False
        leftHalf = num[:len(num)//2]
        rightHalf = num[len(num)//2:]

        leftQuestionMarkCount = len([char for char in leftHalf if char is "?"])
        rightQuestionMarkCount = len([char for char in rightHalf if char is "?"])
        questionMarkCount = leftQuestionMarkCount + rightQuestionMarkCount

        # Case 1: If there is an odd number of "?", Alice gets the final move
        if questionMarkCount % 2 == 1:
            return True

        # Case 2: If there is an even (including 0) number of "?" on both sides
        if leftQuestionMarkCount == rightQuestionMarkCount:
            leftSum = sum([int(n) for n in leftHalf if n.isdigit()])
            rightSum = sum([int(n) for n in rightHalf if n.isdigit()])
            return bob if leftSum == rightSum else alice
        
        # Case 3: There is more "?" on left side
        if leftQuestionMarkCount > rightQuestionMarkCount:
            extra = leftQuestionMarkCount - rightQuestionMarkCount
            leftSum = sum([int(n) for n in leftHalf if n.isdigit()])
            rightSum = sum([int(n) for n in rightHalf if n.isdigit()])
            if (rightSum - leftSum) == extra // 2 * 9:
                return bob
            else:
                return alice
        
        if leftQuestionMarkCount < rightQuestionMarkCount:
            extra = rightQuestionMarkCount - leftQuestionMarkCount
            leftSum = sum([int(n) for n in leftHalf if n.isdigit()])
            rightSum = sum([int(n) for n in rightHalf if n.isdigit()])
            if (leftSum - rightSum) == extra // 2 * 9:
                return bob
            else:
                return alice

        

