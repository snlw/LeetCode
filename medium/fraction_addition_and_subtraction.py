"""
https://leetcode.com/problems/fraction-addition-and-subtraction/submissions/1365319168/?envType=daily-question&envId=2024-08-23

TC: O(n), where n is the number of fractions
SC: O(d), where d is the number of unique denominators
"""
class Solution:
    def fractionAddition(self, expression: str) -> str:
        fractionMap = {}

        # Split by "/"
        nums = [section for section in re.split("/|(?=[+-])", expression) if section]

        for i in range(0, len(nums) - 1, 2):
            numerator = nums[i]
            denominator = nums[i + 1]
            if denominator not in fractionMap:
                fractionMap[denominator] = 0
            fractionMap[denominator] += int(numerator)
        
        ansN, ansD = 0, 0
        
        for d, n in fractionMap.items():
            if n == 0:
                continue

            if ansN == 0 and ansD == 0:
                ansN, ansD = int(n), int(d)
                continue

            # Find lowest common multiple
            lcm = math.lcm(ansD, int(d))
            ansN = ansN*(lcm // ansD) + int(n)*(lcm // int(d))
            ansD = lcm
        
        if ansN == 0:
            return "0/1"
        else:
            gcd = math.gcd(ansN, ansD)
            return str(ansN // gcd) + "/" + str(ansD // gcd)
        

