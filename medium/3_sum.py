# https://leetcode.com/problems/3sum/submissions/1279175616/

# Time Complexity: O(n^2)
# Space Complexity: O(n)

# Type: Arrays
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        
        # Split numbers
        negative, positive, zero = [], [], []
        for num in nums:
            if num == 0:
                zero.append(num)
            elif num > 0:
                positive.append(num)
            else:
                negative.append(num)
        
        uniqueNegatives, uniquePositives = set(negative), set(positive)

        # Case 1: 1 zero exists in solution, [-1, 0, 1]
        if zero:
            for n in uniqueNegatives:
                if n*-1 in uniquePositives:
                    ans.add((n, 0, n*-1))

        # Case 2: 3 zeros exists in solution, [0, 0, 0]
        if len(zero) >= 3:
            ans.add((0,0,0))

        # Case 3: 2 negatives exists in solution, [-1, -1, 2]
        for i in range(len(negative)):
            for j in range(i+1, len(negative)):
                totalNegative = negative[i] + negative[j]
                if (abs(totalNegative)) in uniquePositives:
                    ans.add(tuple(sorted([negative[i], negative[j], abs(totalNegative)])))
        
        # Case 4: 2 positives exists in solution, [-3, 1, 2]
        for i in range(len(positive)):
            for j in range(i+1, len(positive)):
                totalPositive = positive[i] + positive[j]
                if (-1* totalPositive) in uniqueNegatives:
                    ans.add(tuple(sorted([positive[i], positive[j], -1* totalPositive])))

        return ans

