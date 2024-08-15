"""
https://leetcode.com/problems/lemonade-change/submissions/1356171012/?envType=daily-question&envId=2024-08-15

TC: O(n)
SC: O(1)
"""
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {
            5 : 0,
            10 : 0
        }

        for bill in bills:
            if bill == 5:
                change[5] += 1
            elif bill == 10:
                if change[5] < 1:
                    return False
                change[5] -= 1
                change[10] += 1
            elif bill == 20:
                ## 1 $10 bill and 1 $5 bill as change
                if change[10] > 0 and change[5] > 0:
                    change[10] -= 1
                    change[5] -= 1
                    continue
                ## 3 $5 bills as change
                elif change[5] > 2:
                    change[5] -= 3
                    continue
                return False

        return True
