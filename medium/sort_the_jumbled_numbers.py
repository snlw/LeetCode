"""
https://leetcode.com/problems/sort-the-jumbled-numbers/submissions/1331222052/?envType=daily-question&envId=2024-07-24

TC: O(n log n)
SC: O(n)
"""
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def mapTo(a):
            a = str(a)
            result = ""
            for char in a:
                result += str(mapping[int(char)])
            return int(result)

        mappedValues = [mapTo(num) for num in nums]
        mappedTuples = sorted(zip(nums, mappedValues), key=lambda x: x[1])

        return [m[0] for m in mappedTuples]

