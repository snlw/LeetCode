"""
https://leetcode.com/problems/largest-number/submissions/1394391592/?envType=daily-question&envId=2024-09-18
"""
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a: int, b: int):
            strA, strB = str(a), str(b)
            if int(strA + strB) > int(strB + strA):
                return -1
            else:
                return 1

        nums.sort(key=cmp_to_key(compare))
        if nums[0] == 0:
            return "0"

        return "".join([str(num) for num in nums])
